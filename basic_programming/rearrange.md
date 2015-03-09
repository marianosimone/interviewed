# Given an array of elements and another of numbers defining its order, rearrange the first to match the second

Example given:

    >>> rearrange(['a', 'c', 'd', 'b'], [0, 1, 3, 2])
    ['a', 'c', 'b', 'd']

# Implementation

```
def rearrange(elements, positions):
    for i in xrange(len(elements)):
        rearranging = elements[i]
        while positions[i] != i and positions[i] != -1:
            rearranging, elements[positions[i]] = elements[positions[i]], rearranging
            tmp = i
            i = positions[i]
            positions[tmp] = -1
    return elements
```
