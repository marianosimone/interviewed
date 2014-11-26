# Given a string, determine whether or not its openers and closers are properly nested

Let's say:

- '(', '{', '[' are called "openers."
- ')', '}', ']' are called "closers."

## Implementation

```python
    def is_balanced(string):
        '''
        This implementation runs in O(n) (all chars are checked in the worst case), and takes O(n) space (in case all elements are openers)
        >>> is_balanced('{ [ ] ( ) }')
        True
        >>> is_balanced('{ [ ( ] ) }')
        False
        >>> is_balanced('{ [ }')
        False
        '''
        mapper = {'}': '{', ']': '[', ')': '('}
        openers = set(mapper.values())
        closers = set(mapper.keys())
        stack = []
        for c in string:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if not stack or stack[-1] != mapper[c]:
                    return False
                stack.pop()
        return len(stack) == 0
```
