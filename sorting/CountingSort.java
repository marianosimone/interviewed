package ar.com.marianosimone.sorting;

/**
 * Stable
 * Average case O(n+k) (k the max length of the input keys)
 * Good for small-enough keys
**/
public class CountingSort {

    public int[] sort(int[] input) {
        if (input.length <= 1) {
            return input;
        }
        final int max = findMax(input);
        final int[] counter = new int[max+1];
        for (int i = 0; i < input.length; ++i) {
            counter[key(input[i])] += 1;
        }
        for (int i = 1; i < counter.length; ++i) {
            counter[i] += counter[i-1];
        }
        final int[] result = new int[input.length];
        for (int i = input.length-1; i >= 0; --i) {
            final int key = key(input[i]);
            result[counter[key]-1] = input[i];
            counter[key] -= 1;
        }
        return result;
    }

    private int findMax(int[] input) {
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < input.length; ++i) {
            if (input[i] > max) {
                max = input[i];
            }
        }
        return max;
    }

    // Can be redefined to get the key for any type of data
    private int key(final int i) {
        return i;
    }

}
