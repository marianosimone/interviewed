# Implement a Minimal Stack

It should be able to do the following in constant time (O(1)):

- push
- pop
- get the minimum value

## Implementation

```python
class MinimalStack:
    def __init__(self):
        self._stack = []
        self._minimums = []

    def push(self, element):
        if not self._minimums or element <= self._minimums[-1]:
            self._minimums.append(element)
        self._stack.append(element)

    def pop(self):
        if not self._stack:
            raise IndexError("Can't pop from an empty stack")
        e = self._stack.pop()
        if e == self._minimums[-1]:
            self._minimums.pop()
        return e

    def minimum(self):
        if not self._minimums:
            raise IndexError("Can't get the minimum of an empty Stack")
        return self._minimums[-1]
```