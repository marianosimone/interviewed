# Generate permutations of input elements

Example given:

    input = ['A', 'B', 'C', 'D']
    output = ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADCB', 'ADBC', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDCA', 'BDAC', 'CBAD', 'CBDA', 'CABD', 'CADB', 'CDAB', 'CDBA', 'DBCA', 'DBAC', 'DCBA', 'DCAB', 'DACB', 'DABC'] 

## Implementation

```java
public <T> void permutations(final List<T> objects, final int pointer) {
    if (pointer == objects.size()) {
        // "Visit" the permutation
    }
    for (int i = pointer; i < objects.size(); ++i) {
        final List<T> permutation = new ArrayList<T>(objects);
        permutation.set(pointer, objects.get(i));
        permutation.set(i, objects.get(pointer));
        permutations(permutation, pointer+1);
    }    
}
```

# Generate combinations of input elements

Example given:

    input = ['A', 'B', 'C', 'D']
    output = ['A', 'AB', 'ABC', 'ABCD', 'B', 'BC', 'BCD', 'C', 'CD', 'D']

## Implementation

```java
public <T> void combinations(final T[] values, final List<T> current, final int index) {
    for (int i = index; i < values.length; ++i) {
        current.add(values[i]);
        // "Visit" the combination
        combinations(values, current, i+1);
        current.remove(current.size()-1);
    }    
}
```
