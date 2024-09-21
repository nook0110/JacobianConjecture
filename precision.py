class Precision:
    def __init__(self, precision_of_phc_solver = 'd', chop = 1e-15, accuracy = 30) -> None:
        self.__precision = precision_of_phc_solver
        self.__chop = chop
        self.__accuracy = accuracy

    def get_precision(self) -> str:
        return self.__precision

    def get_chop(self) -> float:
        return self.__chop
    
    def get_accuracy(self) -> int:
        return self.__accuracy
    
