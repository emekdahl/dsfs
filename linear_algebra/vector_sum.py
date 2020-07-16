from typing import List

from vectors import Vector

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    num_elements = len(vectors[0])

    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors)

        for i in range(num_elements)]

    assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]