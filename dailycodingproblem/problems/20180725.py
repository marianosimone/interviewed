# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def _count_univals(root):
    """
    Count the amount of subtrees that are univals, as well as the value of unival tree the node is
    a root of or null if it's not
    """
    if not root:
        return (0, None, None)
    left = _count_univals(root.left)
    right = _count_univals(root.right)
    is_unival = (right[1] is None or right[1] == root.value) and (left[1] is None or left[1] == root.value)
    return (
        (1 if is_unival else 0) + left[0] + right[0],
        root.value if is_unival else None
    )

def count_univals(root):
    univals = _count_univals(root)
    return univals[0]

import pytest

@pytest.mark.parametrize(('tree', 'expected'), [
    (Node(1), 1),
    (Node(2), 1),
    (Node(0, Node(1)), 1),
    (Node(0, Node(1), Node(0)), 2),
    (Node(0, Node(1), Node(0, Node(1), Node(0))), 3),
    (Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))), 5)
])
def test(tree, expected):
    assert count_univals(tree) == expected
