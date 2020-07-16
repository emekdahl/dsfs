import math
from vectors import Vector
from magnitude import magnitude
from subtract_vectors import subtract

def distance(v: Vector, w: Vector) -> float:

    return magnitude(subtract(v,w))
