# Complete the preOrder function in the editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's preorder traversal as a single line of space-separated values.

# Input Format

# Our test code passes the root node of a binary tree to the preOrder function.

# Output Format

# Print the tree's preorder traversal as a single line of space-separated values.

# Sample Input

#      1
#       \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4  

# Sample Output

# 1 2 5 3 4 6 

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)