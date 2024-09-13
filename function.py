from random_point import generate_random_point
import sympy
import phcpy.solver

class Function:
    def __init__(self, polynomials : list[sympy.poly]):
        self.__polynomials = polynomials
        self.__degree = None
        self.__vars = [f'x_{i}' for i in range(1, len(polynomials) + 1)]

    def __str__(self) -> str:
        answer = ""
        for i in range(1, len(self.__polynomials) + 1):
            answer += f'x_{i} -> {self.__polynomials[i]}, '
        return answer
    
    def solve(self, point):
        assert(len(point) == len(self.__polynomials))

        H = list(map(lambda function, coord : f'{function - coord};', zip(self.__polynomials, point)))
        solutions = []
        try:
            for solution in phcpy.solver.solve(H, tasks=2, dictionary_output=True):
                sol = list(map(lambda var, solution = solution : solution[var], self.__vars))
                solutions.append(sol)
        except:
            return None
        return list(set(solutions))
    
    def get_jacobian(self) -> sympy.Matrix:
        F = sympy.Matrix(self.__polynomials)
        return F.jacobian(self.__vars)
    
    def __evaluate_potential_field_extension_degree(self) -> int:
        points_checked = 0
        max_checks = 30
        cur_degree = 0
        while points_checked < max_checks:
            point = generate_random_point()
            solutions = self.solve(point)
            if solutions is None:
                self.contracts_ = True
                return
            points_checked += 1
            cur_degree = max(cur_degree, len(solutions))
            if cur_degree >= sympy.total_degree(self.__first) * sympy.total_degree(self.__second):
                break
        return cur_degree
    @property
    def degree(self):
        if self.__degree is None:
            self.__degree = self.__evaluate_potential_field_extension_degree()
        return self.__degree

    __polynomials : list[sympy.poly]
    __degree : int
    contracts_ : bool
