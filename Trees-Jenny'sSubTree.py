# Jenny loves experimenting with trees. Her favorite tree has n nodes connected by n-1 edges, and each edge is unit in length. She wants to cut a subtree(i.e., a connected part of the original tree) of radius r from this tree by performing the following two steps:

# Choose a node, r, from the tree.
# Cut a subtree consisting of all nodes which are not further than r units from node x.

# Given n, r, and the definition of Jenny's tree, find and print the number of different subtrees she can cut out. Two subtrees are considered to be different if they are not isomorphic.

# Input Format

# The first line contains two space-separated integers denoting the respective values of n and r.
# Each of the next n-1 subsequent lines contains two space-separated integers, x and y, describing a bidirectional edge in Jenny's tree having length 1.

# Output Format

# Print the total number of different possible subtrees.

# Sample Input 0

# 7 1
# 1 2
# 1 3
# 1 4
# 1 5
# 2 6
# 2 7

# Sample Output 0

# 3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = jennysSubtrees(n, r, edges)

    fptr.write(str(result) + '\n')

    fptr.close()