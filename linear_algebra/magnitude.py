import math
from vectors import Vector
from sum_of_squares import sum_of_squares

def magnitude(v: Vector) -> float:

    return math.sqrt(sum_of_squares(v))

    assert magnitude([3, 4]) == 5