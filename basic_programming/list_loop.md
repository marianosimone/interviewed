# Given a list with a loop, find the length of it

From [CodeWars](http://www.codewars.com/kata/can-you-get-the-loop)

You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop. Use the "next" attribute to get the following node

# Implementation

```python
def loop_size(node):
    hare = node.next
    tortoise = node
    while hare != tortoise:
        tortoise = tortoise.next
        hare = hare.next.next
    # now both are in the same place... let's start counting until that happens again
    loop_size = 1
    hare = hare.next
    while hare != tortoise:
        loop_size += 1
        hare = hare.next
    return loop_size
```
