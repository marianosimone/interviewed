# Given an array of 2D points, find if (and return) there is a vertical axis of symmetry

For example:

- [(1, 0)] -> 1
- [(1, 0), (2, 0)] -> 1.5
- [(1, 0), (2, 0), (1, 1)] -> None/False

# Implementations

A O(N) solution is:

- Iterate through the array, getting the lower and upper `x` values, and consider the middle between them the candidate vertical axis
- For each point, check if the opposite point (considering that axis) is present

```python
from collections import defaultdict

def find_middle(points):
    lower = points[0][0]
    upper = points[0][0]
    # nicer solutions are possible, but at the expense of iterating the array twice :(
    for x, _ in points:
        if x < lower:
            lower = x
        elif x > upper:
            upper = x
    return (upper + lower)/2.0

def symmetric_vertical_axis(points):
    if not points:
        return None
    middle = find_middle(points)
    missing_symmetric = defaultdict(int)
    for x, y in points:
        if x == middle:
            continue
        if missing_symmetric[(2*middle-x, y)]:
            missing_symmetric[(2*middle-x, y)] -= 1
        else:
            missing_symmetric[(x, y)] += 1
    return middle if all(i == 0 for i in missing_symmetric.values()) else None
```
