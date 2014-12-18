# Given a key and a dictionary, check if the key is composed of an arbitrary number of concatenations of strings from the dictionary

Example given:

Dictionary: "world", "hello", "super", "hell"

- key: "helloworld" --> return true
- key: "superman" --> return false
- key: "hellohello" --> return true

# Implementation

```python
class Trie:
    def __init__(self, words):
        self._data = {}
        for w in words:
            level = self._data
            for l in w:
                if l not in level:
                    level[l] = {}
                level = level[l]
            level[None] = True

    def lookup(self, key):
        level = self._data
        for i, l in enumerate(key):
            if l not in level:
                return key[:i], False
            level = level[l]
        return key, None in level


def is_formed_by_words(key, dictionary):
    discovered = [0]
    target_length = len(key)
    while discovered:
        current = discovered.pop()
        if current == target_length:
            return True
        for i in xrange(current+1, target_length+1):
            match, is_word = dictionary.lookup(key[current:i])
            if match:
                if is_word:
                    discovered.append(i)
            else:
                break
    return False
```
