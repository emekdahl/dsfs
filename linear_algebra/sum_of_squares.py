from vectors import Vector
from dot import dot

def sum_of_squares(v: Vector) -> float:

    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14