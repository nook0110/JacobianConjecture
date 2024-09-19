import random

def generate_random_point(dimensions : int):
    return [random.randrange(-100, 100) for _ in range(0, dimensions)]
