# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

from functools import reduce
from operator import mul

def sum_but_self(elements):
    """
    This implementation is O(n) in time (going over twice), and O(n) in space, and uses division
    """
    total = reduce(mul, elements, 1)
    return [int(total/x) for x in elements]

def accumulate(elements, direction):
    rv = []
    accumulator = 1
    for e in elements[::direction]:
        rv.append(accumulator)
        accumulator *= e
    return rv

def sum_but_self_bonus(elements):
    """
    Bonus: This implementation is a bit uglier, iterates the array 3 times and uses more space, but
    it doesn't use division
    """
    to_left = accumulate(elements, 1)
    to_right = accumulate(elements, -1)[::-1]
    return [to_left[i]*to_right[i] for i in range(len(elements))]

import pytest

@pytest.mark.parametrize('elements, expected', [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [6, 3, 2]),
])
def test_eval(elements, expected):
    assert sum_but_self(elements) == expected
    assert sum_but_self_bonus(elements) == expected
