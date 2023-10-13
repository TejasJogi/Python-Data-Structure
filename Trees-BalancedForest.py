# Greg has a tree of nodes containing integer data. He wants to insert a node with some non-zero integer value somewhere into the tree. His goal is to be able to cut two edges and have the values of each of the three new trees sum to the same amount. This is called a balanced forest. Being frugal, the data value he inserts should be minimal. Determine the minimal amount that a new node can have to allow creation of a balanced forest. If it's not possible to create a balanced forest, return -1.

# For example, you are given node values c = [15, 12, 8, 14, 13] and edges = [[1, 2], [1, 3], [1,4], [4, 5]]. It is the following tree:

# The blue node is root, the first number in a node is node number and the second is its value. Cuts can be made between nodes 1 and 3 and nodes 1 and 4 to have three trees with sums 27, 27 and 8. Adding a new node w of c|w| = 19 to the third tree completes the solution.

# Function Description

# Complete the balancedForest function in the editor below. It must return an integer representing the minimum value of c|w| that can be added to allow creation of a balanced forest, or -1 if it is not possible.

# balancedForest has the following parameter(s):

# c: an array of integers, the data values for each node
# edges: an array of 2 element arrays, the node pairs per edge

# Input Format

# The first line contains a single integer, q, the number of queries.

# Each of the following q sets of lines is as follows:

# The first line contains an integer, n, the number of nodes in the tree.
# The second line contains n space-separated integers describing the respective values of c|1|, c|2|, c|3|,...., c|n|, where each c|i| denotes the value at node i.
# Each of the following n - 1 lines contains two space-separated integers, x|j| and y|j|, describing edge j connecting nodes x|j| and y|j|.

# Output Format

# For each query, return the minimum value of the integer c|w|. If no such value exists, return -1 instead.

# Sample Input

# 2
# 5
# 1 2 2 1 1
# 1 2
# 1 3
# 3 5
# 1 4
# 3
# 1 3 5
# 1 3
# 1 2

# Sample Output

# 2
# -1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#

sys.setrecursionlimit(10**5)

def r():
    return list(map(int, input().split()))

def bin_search(arr, pred, lo=0):
    hi = len(arr)
    while lo < hi:
        mid = (lo+hi)//2
        if pred(arr[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(arr) else None

class UndirectedGraph(object):
    def __init__(self, size):
        self.size = size
        self.M = 0
        self.edges = [set([]) for _ in range(self.size)]

    def add_edge(self, u, v):
        """Adds edge to graph if it doesn't already exist."""
        if v not in self.edges[u]:
            self.edges[u].add(v)
            self.edges[v].add(u)
            self.M += 1

    def neighbors(self, u):
        for v in self.edges[u]:
            yield v

class WeightedTree(UndirectedGraph):
    def __init__(self, size, weights):
        super().__init__(size)
        self.weights = weights
        self.labels = [None]*self.size
        self.cum_weights = [None]*self.size
        self.inverted = [False]*self.size
        self.nextnode = 0
        self.num_children = [None]*self.size
        self.root = 0

    def initialize(self):
        self.set_labels(self.root)
        self.sorted_nodes = sorted(list(range(self.size)), key=lambda x: self.cum_weights[x])

    def set_labels(self, root):
        self.dfs(root, set([]))
        self.total_weight = self.cum_weights[self.root]
        for i, cw in enumerate(self.cum_weights):
            if cw > self.total_weight - cw:
                self.cum_weights[i] = self.total_weight - cw
                self.inverted[i] = True

    def dfs(self, u, visited):
        visited.add(u)
        self.labels[u] = self.nextnode
        self.nextnode += 1
        self.cum_weights[u] = self.weights[u]
        self.num_children[u] = 0
        for v in self.neighbors(u):
            if v not in visited:
                cw, nchildren = self.dfs(v, visited)
                self.cum_weights[u] += cw
                self.num_children[u] += nchildren + 1
        return self.cum_weights[u], self.num_children[u]

    def solve(self):
        tw = self.total_weight
        first_idx = bin_search(self.sorted_nodes, lambda u: self.cum_weights[u] >= (tw+2)//3)
        if first_idx is None:
            return None
        while first_idx < self.size:
            first = self.sorted_nodes[first_idx]
            first_cw = self.cum_weights[first]
            label1 = self.labels[first]
            last_child_label = label1 + self.num_children[first]

            for target_w in (tw - first_cw * 2, first_cw):
                second_idx = bin_search(self.sorted_nodes, lambda u: self.cum_weights[u] >= target_w)
                if second_idx is not None:
                    while (second_idx < self.size and self.cum_weights[self.sorted_nodes[second_idx]] == target_w):
                        second = self.sorted_nodes[second_idx]
                        is_child = label1 < self.labels[second] <= last_child_label
                        is_child = is_child if not self.inverted[first] else not is_child
                        if not is_child and self.labels[second] != label1:
                            return first_cw * 3 - tw
                        second_idx += 1

            first_idx += 1
        if 2*first_cw == tw:
            return first_cw
        return None


def read_input():
    n = int(input())
    weights = r()
    G = WeightedTree(n, weights)
    for _ in range(n-1):
        u, v = r()
        u -= 1
        v -= 1
        G.add_edge(u, v)
    G.initialize()
    return G

def main():
    q = int(input())
    for _ in range(q):
        G = read_input()
        ans = G.solve()
        print(ans if ans is not None else -1)
main()