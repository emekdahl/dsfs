from typing import List
from vectors import Vector

from scalar_multiply import scalar_multiply
from vector_sum import vector_sum


def vector_mean(vectors: List[Vector]) -> Vector:

    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

    assert vector_mean([[1,2], [3,4], [5,6]] == [3,4])