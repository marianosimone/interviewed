# Given a string, determine if a substring is contained in it

## Implementation

```python
def has_substring(string, substring):
    """
    >>> has_substring('abate', 'bat')
    True
    >>> has_substring('bater', 'bat')
    True
    >>> has_substring('arbat', 'bat')
    True
    >>> has_substring('beat', 'bat')
    False
    """
    for starter in range(len(string) - len(substring) + 1):
        for currently_looking_for in range(len(substring)):
            if string[starter+currently_looking_for] != substring[currently_looking_for]:
                break
            if (currently_looking_for == len(substring)-1):
                return True
    return False
```
