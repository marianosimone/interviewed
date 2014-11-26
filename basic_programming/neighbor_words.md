# Given a word, return the possible variations made from spelling errors

- neighbor_chars(c) is available
- is_word(w) is available
- A "variation" is defined as one or more of the characters being changed by one of its neighbors

## Implementation

```python
def neighbor_words(word):
    '''
    Returns a sequence of words that could be formed replacing each letter for any of its neighbors
    This solution is O(m^n), where m is the number of neighbors per character, and n is the lenght of the word
    >>> neighbor_words('hi')
    set(['hi', 'go'])
    '''
    if not word:
        return set()
    return [w for w in _neighbors(word, 0) if is_word(w)]

def _neighbors(word, i):
    '''
    Given a word and an index to start with, return all neighbor words that can be made up from that index on
    '''
    if i > len(word):
        return set([''])  # Base case: from the end on, you can only generate an empty string
    next_neighbors = _neigbors(word, i+1)
    return set([char + neighbor for char in neighbor_chars(word[i] for neighbor in next_neighbors)])
```

## Alternative implementations

An iterative implementation would be:

```python
from itertools import product

def neighbor_words(word):
    return [w for w in set([''.join(p) for p in product([neighbor_chars(c) for c in word])]) if is_word(w)]
```

If only one letter can be changed at a time, a possible implementation, that runs in O(nxm), could be:

```python
def neighbor_words(word):
    words = set()
    for i, c in enumerate(word):
        for n in neighbor_chars(c):
            candidate = '%s%s%s' % (word[:i], n, word[i+1:])
            if is_word(candidate):
                words.add(candidate)
    return words
```

# Possible discussions

- If the dictionary was under our control and we could change implementations to use a TRIE, we could implement a function that, given a word, determines if it COULD be the beginning of a word. That way, we could cut down the recursion/iteration tree as soon as we are building a useless variation
