from function import Function
from check_result import CheckResult

class CheckInfo:
        def __init__(self, function : Function, result : CheckResult, check_amount : int, point : tuple | None = None, value : str | None  = None) -> None:
            self.function_ = function
            self.result_ = result
            self.check_amount_ = check_amount
            self.point_ = point
            self.value_ = value

        function_ : Function
        result_ : CheckResult
        check_amount_ : int
        point_ : tuple | None
        value_ : str | None