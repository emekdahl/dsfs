from vectors import Vector

import os, sys

#Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)

from linear_algebra.dot import dot as dot

def sum_of_squares(v: Vector) -> float:

    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14