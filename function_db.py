import mysql.connector as con
from check_info import CheckInfo

class FunctionDatabase:
    def __init__(self, host : str = 'localhost', user : str = 'root', password : str = 'root', database : str = 'functions') -> None:
        self.connection_ = con.connect(
            host=host,
            user=user,
            password=password,
            database=database)
        self.mycursor_ = self.connection_.cursor()

    def check(self, function : str) -> bool:
        exists = f"SELECT EXISTS(SELECT * FROM functions WHERE Function='{function}')"
        self.mycursor_.execute(exists)
        return self.mycursor_.fetchall()[0][0]

    def insert(self, info : CheckInfo):
        insert = f'''INSERT INTO functions (Function, ExtensionDegree, CheckResult, CheckAmount, Point, Value) VALUES (
        '{info.function_}', 
        {info.function_.get_degree()},
        '{info.result_.name}',
        {info.check_amount_},
        '{info.point_}',
        '{info.value_}'
        );
        '''
        self.mycursor_.execute(insert)