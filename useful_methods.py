# encoding utf-8

def bisect_right(data, target, lo, hi):
    """
    Given a sorted array, returns the insertion position of target
    If the value is already present, the insertion post is to the right of all of them
    >>> bisect_right([1,1,2,3,4,5], 1, 0, 6)
    2
    >>> bisect_right([1,1,2,3,4,5], 0, 0, 6)
    0
    >>> bisect_right([1,1,2,3,4,5], 6, 0, 6)
    6
    """
    while lo < hi:
        mid = (lo+hi)/2
        if data[mid] > target:
            hi = mid
        else:
            lo = mid+1
    return lo

def bisect_left(data, target, lo, hi):
    """
    Given a sorted array, returns the insertion position of target
    If the value is already present, the insertion post is to the left of all of them
    >>> bisect_left([1,1,2,3,4,5], 1, 0, 6)
    0
    >>> bisect_left([1,1,2,3,4,5], 6, 0, 6)
    6
    >>> bisect_left([1,1,2,3,4,5], 0, 0, 6)
    0
    """
    while lo < hi:
        mid = (lo+hi)/2
        if data[mid] < target:
            lo = mid+1
        else:
            hi = mid
    return lo

def permutations_generator(head, tail=[]):
    """
    >>> [p for p in permutations_generator([1, 2, 3])]
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if not head:
        yield tail
    else:
        for i in xrange(len(head)):
            for p in permutations_generator(head[:i] + head[i+1:], tail+[head[i]]):
                yield p

def permutations(data):
    """
    >>> [p for p in permutations([1, 2, 3])]
    [[3, 2, 1], [2, 3, 1], [3, 1, 2], [1, 3, 2], [2, 1, 3], [1, 2, 3]]
    """
    stack = [(data, [])]
    rv = []
    while stack:
        head, tail = stack.pop()
        if not head:
            rv.append(tail)
        else:
            for i in xrange(len(head)-1, -1, -1):
                stack.append((head[:i] + head[i+1:], [head[i]]+tail))
    return rv

class BinaryIndexedTree:
    def __init__(self, length):
        self._data = [0 for i in xrange(length+1)]

    def value(self, pos):
        rv = self._data[pos]
        if (pos > 0):
            z = pos - (pos & -pos)
            pos -= 1
            while (pos != z):
                rv -= self._data[pos]
                pos -= (pos & -pos)
        return rv

    def add(self, pos, count):
        while pos <= len(self._data):
            self._data[pos] += count
            pos += (pos & -pos)

    def accum(self, pos):
        rv = 0
        while (pos > 0):
            rv += self._data[pos]
            pos -= (pos & -pos)
        return rv

def powerset(s):
  """Computes all of the sublists of s"""
  rv = [[]]
  for num in s:
    rv += [x+[num] for x in rv]
  return rv


def lis(arr):
    """
    Return the Longest Increasing Subsequence of arr, in O(N^2)
    >>> lis([2, 1, 3, 4, -5, 3, 2, 4, 5])
    [-5, 2, 4, 5]
    """
    elements = [(0, 1)]
    global_max = (0, 1)
    for i in xrange(1, len(arr)):
        max_before = (i, 1)
        for j in xrange(i-1, -1, -1):
            if arr[i] > arr[j] and elements[j][1]+1 > max_before[1]:
                max_before = (j, elements[j][1]+1)
        elements.append(max_before)
        if max_before[1] > global_max[1]:
            global_max = (i, max_before[1])
    last = len(arr)
    current = global_max
    sequence = []
    while last != current[0]:
        last = current[0]
        sequence.append(arr[current[0]])
        current = elements[current[0]]
    return sequence[::-1]
