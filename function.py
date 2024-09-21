from random_point import generate_random_point
from precision import Precision
import sympy
import phcpy

class Function:
    def __init__(self, polynomials : list[sympy.poly],  precision : Precision):
        self.__precision = precision
        self.__polynomials = polynomials
        self.__degree = None
        self.__vars = sympy.symbols(f'x:{len(polynomials)}')

    def get_precision(self) -> Precision:
        return self.__precision

    def __str__(self) -> str:
        answer = ""
        for i in range(0, len(self.__polynomials)):
            answer += f'{self.__polynomials[i]},'
        return answer[:-1]
    
    def solve(self, point):
        assert(len(point) == len(self.__polynomials))

        H = list(map(lambda function, coord : f'{function - coord};', self.__polynomials, point))
        solutions = []
        for solution in phcpy.solver.solve(H, vrblvl=0, dictionary_output=True, precision=self.__precision.get_precision()):
            sol = tuple(map(lambda var, solution = solution : sympy.N(solution[str(var)], self.get_precision().get_accuracy(), chop=self.__precision.get_chop()), self.__vars))
            solutions.append(sol)
        return list(set(solutions))
    
    def get_jacobian(self) -> sympy.Matrix:
        F = sympy.Matrix(self.__polynomials)
        return F.jacobian(self.__vars)
    
    def __evaluate_potential_field_extension_degree(self) -> int:
        points_checked = 0
        max_checks = 30
        cur_degree = 0
        while points_checked < max_checks:
            point = generate_random_point(len(self.vars))
            solutions = self.solve(point)
            if solutions is None:
                self.contracts_ = True
            points_checked += 1
            cur_degree = max(cur_degree, len(solutions))
        return cur_degree
    
    @property
    def vars(self):
        return self.__vars

    @property
    def degree(self):
        if self.__degree is None:
            self.__degree = self.__evaluate_potential_field_extension_degree()
        return self.__degree

    __polynomials : list[sympy.poly]
    __degree : int
    contracts_ : bool
