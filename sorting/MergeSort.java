package ar.com.marianosimone.sorting;

import java.util.ArrayList;
import java.util.List;

/**
 * Stable
 * Average case O(nlogn)
 * Not in place
 * Good when data is sequential
 * Used for external sorting
**/
public class MergeSort {

    public int[] sort(int[] input) {
        final List<Integer> original = new ArrayList<Integer>(input.length);
        for (int i = 0; i < input.length; ++i) {
            original.add(input[i]);
        }
        final List<Integer> sorted = sort(original);
        final int[] rv = new int[input.length];
        for (int i = 0; i < rv.length; ++i) {
            rv[i] = sorted.get(i);
        }
        return rv;
    }

    private List<Integer> sort(final List<Integer> list) {
        if (list.size() <= 1) {
            return list;
        }
        final int middle = list.size()/2;
        return merge(sort(list.subList(0, middle)), sort(list.subList(middle, list.size())));
    }

    private List<Integer> merge(final List<Integer> left, final List<Integer> right) {
        final List<Integer> result = new ArrayList<Integer>(left.size()+right.size());
        int leftIndex = 0;
        int rightIndex = 0;
        while (rightIndex < right.size() || leftIndex < left.size()) {
            if (rightIndex == right.size()) {
                result.addAll(left.subList(leftIndex, left.size()));
                break;
            } else if (leftIndex == left.size()) {
                result.addAll(right.subList(rightIndex, right.size()));
                break;
            } else {
                if (right.get(rightIndex) < left.get(leftIndex)) {
                    result.add(right.get(rightIndex));
                    rightIndex += 1;
                } else {
                    result.add(left.get(leftIndex));
                    leftIndex += 1;
                }
            }
        }
        return result;
    }

}
