import mysql.connector as con
from check_info import CheckInfo

class FunctionDatabase:
    def __init__(self, host : str = 'localhost', user : str = 'root', password : str = 'root', database : str = 'checked_functions', table : str = 'checked_functions') -> None:
        self.connection_ = con.connect(
            host=host,
            user=user,
            password=password,
            database=database)
        self.table_ = table
        self.mycursor_ = self.connection_.cursor()

    def check(self, function : str) -> bool:
        exists = f"SELECT EXISTS(SELECT * FROM {self.table_} WHERE Function='{function}')"
        self.mycursor_.execute(exists)
        return self.mycursor_.fetchall()[0][0]

    def insert(self, info : CheckInfo):
        return
        insert = f'''INSERT INTO {self.table_} (Phi, ExtensionDegree, CheckResult, CheckAmount, Point, Value) VALUES (
        '{info.function_}', 
        {info.function_.degree},
        '{info.result_.name}',
        {info.check_amount_},
        '{info.point_}',
        '{info.value_}'
        );
        '''
        self.mycursor_.execute(insert)
        self.connection_.commit()
