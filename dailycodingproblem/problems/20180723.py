# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

car = lambda f: f(lambda x, y: x)
cdr = lambda f: f(lambda x, y: y)

import pytest

@pytest.mark.parametrize(('real', 'expected'), [
    (car(cons(3, 4)), 3),
    (cdr(cons(3, 4)), 4),
])
def test(real, expected):
    assert real == expected
