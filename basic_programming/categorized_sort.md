# Given an array of elements categorizable on 3 kinds of priorities, sort them

"Patient files" have 3 types: 'High-importance', 'Mid-importance', 'Low-importance' which are in an arbitrary order (unsorted).

The output preference should start with the highest.

1. High-importance
2. Mid-importance
3. Low-importance
"""

# Implementations

A "[Dutch National Flag](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)" approach, with O(N) time and O(1) space complexity

```python
def arrange(array, key, middle_value):
    current = low_top = 0
    high_bottom = len(array)-1
    while current <= high_bottom:
        if key(array[current]) < middle_value:
            array[current], array[low_top] = array[low_top], array[current]
            current += 1
            low_top += 1
        elif key(array[current]) > middle_value:
            array[current], array[high_bottom] = array[high_bottom], array[current]
            high_bottom -= 1
        else:
            current += 1
    return array
```

# Alternative implementations

Using count sort, it's easy to extend to more than just 3 categories, but space complexity is O(N)

```python
def arrange_count_sort(array, key, values):
    counter = {v: 0 for v in values}
    for i in array:
        counter[key(i)] += 1
    total = 0
    for v in values:
        old = counter[v]
        counter[v] = total
        total += old
    out = [None for i in range(len(array))]
    for i in array:
        out[counter[key(i)]] = i
        counter[key(i)] += 1
    return out
```
