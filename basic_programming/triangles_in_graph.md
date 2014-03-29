# Given a Graph, find all triangles formed by its nodes

Example given:

    input: [(0,1), (1,2), (0, 2), (1,3), (0,4)]
    output: (0,1,2)


## Implementation

```python
def find_triangles(edges):
    '''
    >>> find_triangles([(0,1), (1,2), (0, 2), (1,3), (0,4)])
    [(0, 1, 2)]
    >>> find_triangles([(0,1), (1,2), (2,0), (1,3), (0,3)])
    [(0, 1, 2), (0, 1, 3)]
    >>> find_triangles([(0,1), (1,2), (2, 4), (1,3), (0,4)])
    []
    '''
    adjacency = {}
    for e in edges:
        origin = min(e)
        if origin not in adjacency:
            adjacency[origin] = set()
        adjacency[origin].add(max(e))

    triangles = []
    for origin, adjacents in adjacency.iteritems():
        for middle_node in adjacents:
            for third_node in (adjacents-set([middle_node])):
                if (third_node in adjacency) and (middle_node in adjacency[third_node]):
                    triangles.append(tuple(sorted([origin, middle_node, third_node])))  # sorting just to know in which order it's going to be in output

    return triangles
```

## Alternative implementations

- Do a depth-first search, and when you reach to three steps, check if you are were you started. This approach is easy to scale to more than triangles (ploygons with N sides)
