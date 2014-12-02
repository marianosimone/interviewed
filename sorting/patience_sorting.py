class Pile(list):
    def __lt__(self, o):
        return self[-1] < o[-1]

def find_binary_position(arr, element, begin, end):
    '''
    Given a sorted array, return the position where it is or should be.
    Note that, unless the element is already in the array,
    the method is not guaranteed to return a valid array pos (might be -1 or the length)
    >>> find_binary_position([], 0, 0, -1)
    0
    >>> find_binary_position([1, 2], 0, 0, 1)
    0
    >>> find_binary_position([1, 3], 2, 0, 1)
    1
    >>> find_binary_position([1, 3], 4, 0, 1)
    2
    >>> find_binary_position([1, 3], 1, 0, 1)
    0
    '''
    if end < begin:
        return begin
    middle = end-begin/2
    if arr[middle] < element:
        return find_binary_position(arr, element, middle+1, end)
    return find_binary_position(arr, element, begin, middle-1)

def patience_split(ar):
    '''
    Given a sequence of elements, split them in piles that conform the Patience Sorting algorithm:
    http://en.wikipedia.org/wiki/Patience_sorting
    >>> patience_split([])
    []
    >>> patience_split([1, 2, 3])
    [[1], [2], [3]]
    >>> patience_split([3, 2, 1])
    [[3, 2, 1]]
    >>> patience_split([3, 2, 4, 5])
    [[3, 2], [4], [5]]
    '''
    if not ar:
        return ar
    stacks = []
    for e in ar:
        new = Pile()
        new.append(e)
        pos = find_binary_position(stacks, new, 0, len(stacks)-1)
        if pos == -1:
            stacks.insert(0, new)
        elif pos >= len(stacks):
            stacks.append(new)
        else:
            stacks[pos].append(e)
    return stacks

import heapq

def patience_sort(ar):
    '''
    >>> patience_sort([3, 2, 4, 1])
    [1, 2, 3, 4]
    '''
    piles = patience_split(ar)
    heap = []
    for p in piles:
        heapq.heappush(heap, p)
    for i in xrange(len(ar)):
        pile = heapq.heappop(heap)
        ar[i] = pile.pop(-1)
        if pile:
            heapq.heappush(heap, pile)
    return ar
