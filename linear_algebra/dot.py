from vectors import Vector

def dot(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w), "vectors must be the same length"

    return sum(v_i * w_i for v_i, w_i in zip(v,w))


assert dot([1,2,3], [4,5,6]) == 32