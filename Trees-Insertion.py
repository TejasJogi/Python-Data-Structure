# You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. You just have to complete the function.

# Input Format

# You are given a function,

# Node * insert (Node * root ,int data) {

# }

# Output Format

# Return the root of the binary search tree after inserting the value into the tree.

# Sample Input

#         4
#        / \
#       2   7
#      / \
#     1   3

# The value to be inserted is 6.

# Sample Output

#          4
#        /   \
#       2     7
#      / \   /
#     1   3 6

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            curr = curr.root

            while True:
                if val < curr.info:
                    if curr.left:
                        curr = curr.left
                        break
                    else:
                        curr.left = Node(val)
                elif val > curr.info:
                    if curr.right:
                        curr = curr.right
                        break
                    else:
                        curr.right = Node(val)
                else:
                    break