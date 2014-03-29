# Given a list of numbers, return the pairs for which the sum is leq than k

Example given:

    input: l = [5,7,8,1,3,2], k = 5
    output: [(1,2), (1,3), (2,3)]

## Possible discussions:

- With n being small enough, brute force might be the best option
- What are the best sorting methods for this array?

## Implementation

The idea is that, if you sort the array, you can find a point from which all sums will be greater than K, so you can stop trying out.
Sorting should be around O(NlogN), and then O(NlogN) iterate all elements and search for that point

```python
def pairs_that_sum_less_than_k(elements, k):
    """
    >>> pairs_that_sum_less_than_k([5,7,8,1,3,2], 5)
    [(1, 2), (1, 3), (2, 3)]
    >>> pairs_that_sum_less_than_k([0,1,3,4,5], 5)
    [(0, 1), (0, 3), (0, 4), (0, 5), (1, 3), (1, 4)]
    >>> pairs_that_sum_less_than_k([0,0,0,1], 5)
    [(0, 0), (0, 0), (0, 1), (0, 0), (0, 1), (0, 1)]
    >>> pairs_that_sum_less_than_k([5,6,7], 2)
    []
    """
    sorted_elements = sorted(elements)
    result = []
    for i, e in enumerate(sorted_elements):
        limit = binary_search(sorted_elements, k, e, i, len(sorted_elements))
        for j in range(i+1, limit):
            result.append((e, sorted_elements[j]))
    return result

def binary_search(elements, target, base, begin, end):
    if (begin >= end):
        return begin
    middle = begin+((end-begin)/2)
    result = base + elements[middle]
    if result == target:
        return middle+1
    if result < target:
        return binary_search(elements, target, base, middle+1, end)
    return binary_search(elements, target, base, begin, middle)
```

## Alternative implementations

- Brute force each combination:

```python
result = []
for i, e in enumerate(elements):
    for j in range(i+1, len(elements)):
        if (e + elements[j]) <= k:
            result.append((e, elements[j]))
return result
```
