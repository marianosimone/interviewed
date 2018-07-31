# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
# Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return serialize(self)
    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

from collections import Counter


def serialize(node):
    if not node:
        return ""
    if not node.left and not node.right:
        return str(node.val)
    return "{}[{},{}]".format(node.val, serialize(node.left), serialize(node.right))

def deserialize(string):
    stash = []
    current = ''
    for e in string:
        if e == ',' or e == '[':
            if current:
                stash.append(Node(current))
            else:
                stash.append(None)
            current = ''
        elif e == ']':
            if current:
                stash.append(Node(current))
            else:
                stash.append(None)
            print("Got to the end of the stash:")
            print("Current is", current)
            print("At the top we have", stash[-1], stash[-2], stash[-3])
            right = stash.pop()
            left = stash.pop()
            stash[-1].right = right
            stash[-1].left = left
            print("At the top we have", stash)

            current = ''
        else:
            current += e
    if current:
        return Node(current)
    print(stash)
    return stash[-1]

import pytest



@pytest.mark.parametrize(('node', 'expected'), [
    # (Node('root'), 'root'),
    # (Node('root', Node('left'), Node('right')), 'root[left,right]'),
    (Node('root', Node('left', Node('left.left')), Node('right')), 'root[left[left.left,],right]'),
])
def test(node, expected):
    # assert serialize(node) == expected
    # print(deserialize(expected))
    # print(node)
    assert deserialize(expected) == node
