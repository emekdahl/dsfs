from vectors import Vector

def add(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)

    return [v_i + w_i for v_i, w_i in zip(v,w)]


assert add([1,2,3], [4,5,6]) == [5,7,9]