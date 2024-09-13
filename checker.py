from function import Function
from check_result import CheckResult 
from random_point import generate_random_point
from typing import Any
import logging
import sympy

class Checker:
    def __init__(self, function : Function) -> None:
        self.function_ = function
        self.jacobian_ = function.get_jacobian()
        self.det_ = self.jacobian_.det()
        self.logger_ = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
    
    @staticmethod
    def is_finite_solutions(solutions) -> bool:
        from sympy import sympify
        for value in solutions:
            expr = sympify(value)
            symbols = expr.free_symbols
            if symbols:
                return False
        return True
    
    def calculate(self, solutions):
        x, y = sympy.symbols('x y')
        values = []
        for solution in solutions:
            val = self.det_
            val = val.subs(x, solution[0])
            val = val.subs(y, solution[1])
            values.append(val.evalf())
        from itertools import combinations
        ans = sum(map(lambda x : 1/x, values))
        return ans 


    def calculate_for_point(self, point = [0,0]):
        solutions = function.solve(point)
        return self.calculate(solutions) 
    
    def check_solution(self, solutions) -> bool:
        if len(solutions) > self.function_.degree:
            assert(0)
            self.logger_.error("wrong extension degree!")
        return len(solutions) >= self.function_.degree
    
    def test_point(self, point = [0,0]) -> CheckResult:
        self.logger_.info(f"Checking point: {point}")
        solutions = self.function_.solve(point)
        if solutions is None:
            return CheckResult.CONTRACTS
        if not self.check_solution(solutions):
            self.logger_.info(f"Amount of solutions: {len(solutions)} (expected {self.function_.get_degree()})")
            return CheckResult.NON_GENERAL_POSITION
        ev = sympy.sympify(self.calculate(solutions))
        if abs(ev.evalf()) < 0.001:
            return CheckResult.HOLDS
        self.logger_.info(f"Test failed! Eval = {ev.evalf()}")
        return CheckResult.NOT_HOLDS 

    def test(self, iterations = 10):
        self.logger_.info(f"Checking function: {self.function_}")
        general_position_checks = 0
        while general_position_checks < iterations:
            point = generate_random_point()
            result = self.test_point(point)
            self.logger_.info(f"Test result for {point} is: {result.name}")
            if result == CheckResult.CONTRACTS:
                self.logger_.info(f"Contracts at point: {point}")
                return (CheckResult.CONTRACTS, point)
            if result.value == False:
                self.logger_.info(f"Lemma doesn't hold for function: {self.function_}")
                return (CheckResult.NOT_HOLDS, point)
            if result != CheckResult.NON_GENERAL_POSITION:
                general_position_checks += 1
                
        self.logger_.info(f"Lemma holds for function: {self.function_}")
        return (CheckResult.HOLDS, None)
                
    function_ : Function
    jacobian_ : sympy.Matrix
    det_ : Any


        