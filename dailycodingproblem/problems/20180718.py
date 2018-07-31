# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

from collections import Counter


def has_two_elements_that_sum(elements, k):
    """
    This implementation is O(n) in time (going over twice), and O(n) in space
    """
    counter = Counter(elements)
    return any(counter[k - e] >= 1 if k != 2*e else counter[k - e] > 1 for e in elements)

def has_two_elements_that_sum_bonus(elements, k):
    """
    Bonus: This implementation is a bit uglier, but it's still O(n) space and goest over it once
    """
    required = set()
    for e in elements:
        difference = k - e
        if e in required:
            return True
        else:
            required.add(difference)
    return False

import pytest

@pytest.mark.parametrize(('elements', 'k', 'expected'), [
    ([10, 15, 3, 7], 17, True),
    ([-1, 2], 1, True),
    ([10, 10], 20, True),
    ([1, 2, 3], 6, False),
    ([], 1, False),
])
def test_eval(elements, k, expected):
    assert has_two_elements_that_sum(elements, k) == expected
    assert has_two_elements_that_sum_bonus(elements, k) == expected
