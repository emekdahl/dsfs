from typing import List, Tuple
from vectors import Vector

Matrix = List[List[float]]

A = [[1, 2, 3],  # A has 2 rows and 3 columns
    [4, 5, 6]]

B = [[1, 2],     # B has 3 rows and 2 columns
    [3, 4],
    [5, 6]]

def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0

    return num_rows, num_cols

    assert shape([[1,2,3], [4, 5, 6]]) == (2,3)


def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

    assert get_row([[1,2,3], [4, 5, 6]], 0) == ([1,4])
