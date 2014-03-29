# Given a list of words, return all n-grams of adjacent words.

Example given:

    input = ['A', 'B', 'C', 'D']
    output = ['A', 'A B', 'A B C', 'A B C D', 'B', 'B C', 'B C D', 'C', 'C D', 'D']


## Problem variations

- get only n-grams with n >= X

## Implementation

```python
def generate_ngrams(words):
    '''
    >>> generate_ngrams(['A', 'B', 'C', 'D'])
    ['A', 'A B', 'A B C', 'A B C D', 'B', 'B C', 'B C D', 'C', 'C D', 'D']
    >>> generate_ngrams(['A'])
    ['A']
    '''
    ngrams = []
    for i, word in enumerate(words):
        for j in range(i+1, len(words)+1):
            ngrams.append(' '.join([word] + words[i+1:j]))
    return ngrams
```

## Alternative implementations

- In languages where slicing and joining lists is not as easy, a way to buffer a String (Java's StringBuilder, for example) might be a good option inside a loop
