from function import Function
from precision import Precision
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
        checker.test(tests)


    @staticmethod
    def input_function() -> Function:
        n = int(input('variables amount: (2) ') or 2)

        equations = []
        for i in range(0, n):
            equations.append(input(f'x{i}: '))
        return Function(list(map(parse_expr, equations)), precision=Precision('d', 1e-15, 30))
r"""
    *d*: standard double precision (1e-15),

    *dd*: double double precision (1e-30),

    *qd*: quad double precision (1e-60).
"""
main = Main()
main.run()