from function import Function
from check_result import CheckResult 
from random_point import generate_random_point
from typing import Any
import logging
import sympy
from typing import *


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
    
    def calculate(self, solutions) -> int:
        values = []
        for solution in solutions:
            val = self.det_
            for i in range(len(self.function_.vars)):
                val = val.subs(self.function_.vars[i], solution[i])
            values.append(sympy.N(val, self.function_.get_precision().get_accuracy(), chop=self.function_.get_precision().get_chop()))
        from itertools import combinations
        ans = sum(map(lambda x : 1/x, values))
        return ans 


    def calculate_for_point(self, point = [0,0]) -> int:
        solutions = self.function_.solve(point)
        return self.calculate(solutions) 
    
    def check_solution(self, solutions) -> bool:
        if len(solutions) > self.function_.degree:
            self.logger_.error(f"wrong extension degree! expected {self.function_.degree}, but got {len(solutions)}")
        return len(solutions) >= self.function_.degree
    
    def test_point(self, point : list) -> CheckResult:
        self.logger_.info(f"Checking point: {point}")
        solutions = self.function_.solve(point)
        if solutions is None:
            return CheckResult.CONTRACTS
        if not self.check_solution(solutions):
            self.logger_.info(f"Amount of solutions: {len(solutions)} (expected {self.function_.degree})")
            return CheckResult.NON_GENERAL_POSITION
        ev = sympy.N(self.calculate(solutions), self.function_.get_precision().get_accuracy(), chop=self.function_.get_precision().get_chop())
        if ev == 0:
            return CheckResult.HOLDS
        self.logger_.info(f"Test failed! Eval = {ev}")
        return CheckResult.NOT_HOLDS 

    def test(self, iterations = 10) -> Tuple[CheckResult, tuple | None]:
        self.logger_.info(f"Checking function: {self.function_}")
        general_position_checks = 0
        while general_position_checks < iterations:
            point = generate_random_point(len(self.function_.vars))
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


        