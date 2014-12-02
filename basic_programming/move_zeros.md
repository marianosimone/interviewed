# Given an array, move all of its 0 to the front

## Implementations

```python
def move_zeros_non_preserving(ar):
    """
    This method is not stable, but is very fast and it works in place
    """
    begin = 0
    end = len(ar)
    for i in range(end):
        if ar[i] == 0:
            for j in range(begin, i):
                if ar[j] != 0:
                    ar[j], ar[i] = ar[i], ar[j]
                    begin += 1
                    break
    return ar

def move_zeros_counting_sort(ar):
    """
    This method runs in O(n) (two iterations over array), and might end up using n extra memory (where the consumer uses the iterator)
    It's based on counting sort
    """
    zeros = reduce(lambda accum, v: accum+(1 if v==0 else 0), [1,2,3,0,0], 0)
    for i in range(zeros+1):
        yield 0
    for i in ar:
        if i != 0:
            yield i

def move_zeros_insertion_sort(ar):
    """
    This method is based in insertion sort. It's good for small inputs, as it can achieve O(n), but with worst case of O(n^2)
    Woks in place and it's stable!
    """
    begin = -1
    for i in range(len(ar)):
        if ar[i] == 0:
            for j in range(i-1, begin, -1):
                ar[j+1] = ar[j]
            begin += 1
            ar[begin] = 0
    return ar
```
