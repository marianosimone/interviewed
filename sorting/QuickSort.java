package ar.com.marianosimone.sorting;

/**
 * Non-stable
 * Worst-case when array is already sorted O(n^2)
 * Average case O(nlogn)
 * When the array is small enough (~10), it might be optimized using insertion sort
 * Different strategies can be used for selecting the pivot: first, last, middle, median (full array), median (first, middle, last), random
**/
public class QuickSort {

    public int[] sort(final int[] array) {
        quicksort(array, 0, array.length - 1);
        return array;
    }

    private void quicksort(int[] array, int begin, int end) {
        if (begin >= end) {
            return; // array is already sorted
        }
        int low = begin;
        int high = end;
        int pivotIndex = begin;
        int pivotValue = array[pivotIndex];

        while (low < high) {
            while (array[low] <= pivotValue && low < end) {
                low += 1;
            }
            while (array[high] > pivotValue && high > begin) {
                high -= 1;
            }
            if (low < high) {
                swap(array, low, high);
            }
        }
        swap(array, pivotIndex, high);
        quicksort(array, begin, high - 1);
        quicksort(array, low, end);
    }

    private void swap(int[] array, int a, int b) {
        final int tmp = array[a];
        array[a] = array[b];
        array[b] = tmp;
    }

}
