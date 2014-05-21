# Implement a scored docs API

- Recieves a pair (*doc*, *score*) for each scored document in a corpus
- Can return the top *K* elements among the processed elements

## Idea

- Use a Heap to keep track of the best k elements
- Whenever a new doc arrives:
 - If the size of the heap is less than k, add the new doc
 - If not, check its score:
  - If it's better than the worse, remove the worse and add the new one

A Heap will keep the elements sorted and, in general, its implementation allows to remove elements from its tail in O(1), while adding in O(logn)

## Implementation

```python
class ScoredDocsStore:

    def __init__(self, k):
        """
        k is the number of top elements to be returned when asked for top
        """
        self._store = Heap()
        self._k = k

    def register(self, doc, score):
        if len(self._store) < self._k:
            self._store.add((doc, score))
        else:
            if score > self._store[-1]:
                self._store.pop()
                self._store.add((doc, score))

    def top(self):
        return self._store  # This could be changed to just return the docs, not the scores
```