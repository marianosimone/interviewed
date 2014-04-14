package ar.com.marianosimone.sorting;

/**
 * Stable
 * Worst-case when array is inversed O(n^2)
 * Best-case when array is sorted O(n)
 * Good for small inputs
**/
public class InsertionSort {

    public int[] sort(final int[] input) {
        for (int i = 1; i < input.length; ++i) {
            final int value = input[i];
            int j = i;
            while (j > 0 && input[j-1] > value) {
                input[j] = input[j-1];
                j -= 1;
            }
            input[j] = value;
        }
        return input;
    }
}
