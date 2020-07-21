from collections import Counter
from typing import List

import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25]

num_friends_even = [100, 49, 41, 40, 25, 33]

# Central Tendencies

def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

assert mean(num_friends) == 51


def _median_odd(xs:List[float]) -> float:
    """ if len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

assert _median_odd(num_friends) == 41


def _median_even(xs:List[float]) -> float:
    """ if len(xs) is even, the median is the average of the two middle elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2

    return (sorted(xs)[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

assert _median_even(num_friends_even) == 40.5

def median(v: List[float]) -> float:
    """Finds the middle-most value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

print(median(num_friends))
