from function_db import FunctionDatabase
from function import Function
from checker import Checker
from check_info import CheckInfo
from sympy import parse_expr, N

class Main:
    def __init__(self) -> None:
        self.function_db_ = FunctionDatabase()
        #self.init_sql()

    def run(self, precision = 'd') -> None:
        func = self.input_function()
        checker = Checker(func)
        tests = 20
        result, point = checker.test(tests)

        value = None
        if point:
            value = N(checker.calculate_for_point(point), chop=1e-15)
        
        self.function_db_.insert(CheckInfo(func, result, tests, point, value))

    def init_sql(self) -> None:
        print("Connecting to mySQL...")
        host = input("host: (localhost) ") or 'localhost'
        user = input("user: (root) ") or 'root'
        password = input("password: (root) ") or 'root'
        database = input("database: (checked_functions) ") or 'checked_functions'
        table = input("table: (checked_functions) ") or 'checked_functions'
        self.function_db_ = FunctionDatabase(host, user, password, database, table)
    
    @staticmethod
    def input_function() -> Function:
        n = int(input('variables amount: (2) ') or 2)

        equations = []
        for i in range(0, n):
            equations.append(input(f'x{i}: '))
        return Function(list(map(parse_expr, equations)))

main = Main()
main.run()