package ar.com.marianosimone.sorting;

/**
 * Non-stable
 * Average case O(nlogn)
**/
public class HeapSort {

    public int[] sort(int[] input) {
        heapify(input);

        int end = input.length - 1;
        while (end > 0) {
            swap(input, end, 0);
            end -= 1;
            siftDown(input, 0, end);
        }
        return input;
    }

    private void heapify(int[] input) {
        int start = (int) Math.floor((input.length - 2) / 2);
        while (start >= 0) {
            siftDown(input, start, input.length - 1);
            start -= 1;
        }
    }

    private void siftDown(int[] input, int start, int end) {
        int root = start;
        while (root * 2 + 1 <= end) {
            int child = root * 2 + 1;
            int swap = root;
            if (input[swap] < input[child]) {
                swap = child;
            }
            if (child + 1 <= end && input[swap] < input[child + 1]) {
                swap = child + 1;
            }
            if (swap != root) {
                swap(input, root, swap);
                root = swap;
            } else {
                return;
            }
        }
    }

    private void swap(int[] input, int a, int b) {
        final int tmp = input[a];
        input[a] = input[b];
        input[b] = tmp;
    }
}