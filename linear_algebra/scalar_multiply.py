from typing import List

from vectors import Vector

def scalar_multiply(c: float, v: Vector) -> Vector:

    return [c * v_i for v_i in v]

    assert scalar_multiply(2, [1,2,3] == [2,4,6])