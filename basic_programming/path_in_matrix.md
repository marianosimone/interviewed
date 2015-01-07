# Given an NxN matrix with all the values between 1 and N^2, find the starting point and longest consecutive path

- You can move in all 8 directions
- Path needs to be consecutive (1->2->3 is right, but 1->2->4 is not)

# Implementation

Just going through the matrix as if it was a graph

```python

variations = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def neighbors(matrix, i, j):
    return [matrix[i+di][j+dj] for di, dj in variations if (0 <= i+di < len(matrix)) and (0 <= j+dj < len(matrix))]

def find_longest_path(matrix):
    length = len(matrix)**2
    data = [0 for _ in xrange(length+1)]
    indexes = range(len(matrix))
    for i in indexes:
        for j in indexes:
            value = matrix[i][j]
            data[matrix[i][j]] = 1 if value+1 in neighbors(matrix, i, j) else 0

    start = -1
    longest = 0
    current_start = -1
    current = 1

    for i, e in enumerate(data):
        if e == 1:
            current += 1
            if current_start == -1:
                current_start = i
        else:
            if current > longest:
                longest = current
                start = current_start
            current = 1
            current_start = -1
    return start, longest
```

# Alternative Implementation

- Iterate the matrix, and use the value in it as an index for an array which elements are the coordinates as (i,j) pairs
- Iterate the array, and consider the path to be longer if the (i, j) pair in each position is a neighbor of the previous one
