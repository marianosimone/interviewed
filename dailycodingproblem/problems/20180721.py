# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


from collections import Counter


def first_positive_missing(array):
    base_index = 0
    for i, e in enumerate(array):
        if e <= 0:
            array[base_index], array[i] = e, array[base_index]
            base_index += 1

    for e in array[base_index:]:
        index = base_index + e - 1
        if base_index + index <= len(array):
            array[index] = -1

    for i, e in enumerate(array[base_index:]):
        if e != -1:
            return max(base_index, 1) + i
    return 1 + len(array[base_index:]) 

import pytest

@pytest.mark.parametrize(('array', 'expected'), [
    ([3, 4, -1, 1], 2),
    ([1, 2, 0], 3),
    ([1, 2], 3),
    ([], 1),
    ([1, 10000], 2),
    ([-1, -2], 1),
])
def test(array, expected):
    assert first_positive_missing(array) == expected
