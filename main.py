from function_db import FunctionDatabase
from function import Function
from checker import Checker
from sympy import parse_expr

class Main:
    def __init__(self) -> None:
        self.init_sql()

    def run(self) -> None:
        checker = Checker(self.input_function())
        checker.test()

    def init_sql(self) -> None:
        print("Connecting to mySQL...")
        host = input("host: (localhost) ") or 'localhost'
        user = input("user: (root) ") or 'root'
        password = input("password: (root) ") or 'root'
        database = input("database: (checked_functions) ") or 'checked_functions'
        self.function_db_ = FunctionDatabase(host, user, password, database)
    
    @staticmethod
    def input_function() -> Function:
        phi_x = input('phi_x: ')
        phi_y = input('phi_y: ')
        return Function(parse_expr(phi_x), parse_expr(phi_y))

main = Main()
main.run()