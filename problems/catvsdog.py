# coding=utf-8

# Problem: Cats vs Dogs
#
# Description:
#
# The latest reality show has hit the TV: "Cat vs. Dog".
# In this show, a bunch of cats and dogs compete for the very prestigious Best Pet Ever title.
# In each episode, the cats and dogs get to show themselves off,
# after which the viewers vote on which pets should stay and which should be forced to leave the show.
#
# Each viewer gets to cast a vote on two things: one pet which should be kept on the show, and one pet which should be thrown out.
# Also, based on the universal fact that everyone is either a cat lover (i.e. a dog hater) or a dog lover (i.e. a cat hater),
# it has been decided that each vote must name exactly one cat and exactly one dog.
#
# Ingenious as they are, the producers have decided to use an advancement procedure which guarantees that
# as many viewers as possible will continue watching the show: the pets that get to stay will be chosen so as to maximize
# the number of viewers who get both their opinions satisfied. Write a program to calculate this maximum number of viewers.
#
# Input:
# On the first line one positive number: the number of testcases, at most 100. After that per testcase:
#
# One line with three integers c, d, v (1 ≤ c, d ≤ 100 and 0 ≤ v ≤ 500): the number of cats, dogs, and voters.
# v lines with two pet identifiers each:
# - The first is the pet that this voter wants to keep,
# - the second is the pet that this voter wants to throw out.
# A pet identifier starts with one of the characters ‘C’ or ‘D’, indicating whether the pet is a cat or dog, respectively.
# The remaining part of the identifier is an integer giving the number of the pet (between 1 and c for cats, and between 1 and d for dogs).
# So for instance, “D42” indicates dog number 42.
#
# Output:
# Per testcase:
# One line with the maximum possible number of satisfied voters for the show.
#
# Sample input
# 2
# 1 1 2
# C1 D1
# D1 C1
# 1 2 4
# C1 D1
# C1 D1
# C1 D2
# D2 C1
# Sample output
# 1
# 3
#
# Solution Idea:
#
# The first breaktrough is that "based on the universal fact that everyone is either a cat lover", we can
# think about the problem as a bipartite one, in which all votes can be categorized as being from "Cat" or "Dog" lovers
# From there, we can consider each vote a node in a graph, and the fact that one vote contradicts another, an edge
# (i.e. if a vote wants D1 to stay, it contradicts any vote where D1 is wanted to leave)
# The second breakthrough is that, given that the graph is bipartite, in each connected component you can select either
# all votes from one category, or from the other, but not from both (i.e. once you select a vote from one category,
# all its contradictions - members of the other category - can't be selected, thus opening up the possibility to add
# a new element of the original one)
#

from collections import defaultdict

class Vote:
    """
    Represents a type of vote and how many people made it.
    As votes are either from Cat lovers or Dog lovers, they can be categorized by looking at who they love
    """
    def __init__(self, keep, remove):
        self.keep = keep
        self.remove = remove
        self.voters = 1

    def add_voter(self):
        self.voters += 1

    def contradicts(self, other):
        return self.category() != other.category()

    def category(self):
        return self.keep[0]

    def __int__(self):
        return self.voters

    def __hash__(self):
        return hash('%s%s' % (self.keep, self.remove))

    def __eq__(self, other):
        return self.keep == other.keep and self.remove == other.remove

    def __repr__(self):
        return '%s:%s x %d' % (self.keep, self.remove, self.voters)


def votes_as_graph(nodes):
    votes = {}
    graph = defaultdict(list)
    for _ in xrange(nodes):
        key = raw_input()
        if key in votes:
            votes[key].add_voter()
        else:
            keep, remove = key.split(' ')
            vote = Vote(keep, remove)
            votes[key] = vote
            contradictions = [o for o in graph if o.contradicts(vote)]
            for o in contradictions:
                graph[o].append(vote)
                graph[vote].append(o)
        graph[vote]  # Ensure vote in graph, even if there are no contradictions
    return graph

def find_connected_components(graph):
    components = []
    visited_nodes = set()
    for v in graph:
        if v not in visited_nodes:
            visited_nodes.add(v)
            current_component = []
            stack = [v]
            while stack:
                current = stack.pop()
                current_component.append(current)
                for n in graph[current]:
                    if n not in visited_nodes:
                        visited_nodes.add(n)
                        stack.append(n)
            components.append(current_component)
    return components

def categorized_sum(elements, categorizer):
    """
    Given list of elements, return the sum of its values, grouped by category
    """
    result = defaultdict(int)
    for e in elements:
        result[categorizer(e)] += int(e)
    return result

cases = int(raw_input())
for i in xrange(cases):
    c, d, v = [int(i) for i in raw_input().split()]
    graph = votes_as_graph(v)
    components = find_connected_components(graph)
    result = sum(max(categorized_sum(c, lambda v: v.category()).values()) for c in components)
    print result
