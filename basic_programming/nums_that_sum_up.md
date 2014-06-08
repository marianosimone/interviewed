# Given some stored values, find combinations that sum up a value

Should implement:

- store(int)
- test(int), which gives a list of combinations of stored values that sum up to the parameter

## Implementation

```python
class SumUp:

    def __init__(self):
        self.values = set()

    def store(self, value):
        self.values.add(value)

    def test(self, value):
        return [(v, value-v) for v in self.values if value-v in self.values]
        return set([(max(v, value-v), min(v, value-v)) for v in self.values if value-v in self.values])  # if you want to avoid dupes
        return set([(max(v, value-v), min(v, value-v)) for v in self.values if (value-v in self.values) and value-v != v])  # if you want to avoid re-using the same number
```