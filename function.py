from random_point import generate_random_point
import sympy
import phcpy.solver

class Function:
    def __init__(self, polynomials : list[sympy.poly]):
        self.__polynomials = polynomials
        self.__degree = None
        self.__vars = sympy.symbols(f'x:{len(polynomials)}')

    def __str__(self) -> str:
        answer = ""
        for i in range(0, len(self.__polynomials)):
            answer += f'{self.__polynomials[i]},'
        return answer[:-1]
    
    def solve(self, point):
        assert(len(point) == len(self.__polynomials))

        H = list(map(lambda function, coord : f'{function - coord};', self.__polynomials, point))
        solutions = []
        for solution in phcpy.solver.solve(H, tasks=2, dictionary_output=True, precision='d'):
            sol = tuple(map(lambda var, solution = solution : sympy.N(solution[str(var)], chop=1e-15), self.__vars))
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
