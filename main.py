from function import Function
from checker import Checker
from check_info import CheckInfo
from sympy import parse_expr, N

class Main:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        func = self.input_function()
        checker = Checker(func)
        tests = 20
        result, point = checker.test(tests)

        value = None
        if point:
            value = N(checker.calculate_for_point(point), chop=1e-15)
        
        self.function_db_.insert(CheckInfo(func, result, tests, point, value))

    @staticmethod
    def input_function() -> Function:
        n = int(input('variables amount: (2) ') or 2)

        equations = []
        for i in range(0, n):
            equations.append(input(f'x{i}: '))
        return Function(list(map(parse_expr, equations)))

main = Main()
main.run()