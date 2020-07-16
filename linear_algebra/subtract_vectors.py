from vectors import Vector

def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)

    return [v_i - w_i for v_i, w_i in zip(v,w)]


assert subtract([5,7,9], [4,5,6]) == [1,2,3]