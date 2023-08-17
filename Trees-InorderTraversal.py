# In this challenge, you are required to implement inorder traversal of a tree.

# Complete the inOrder function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's inorder traversal as a single line of space-separated values.

# Input Format

# Our hidden tester code passes the root node of a binary tree to your $inOrder* function.

# Output Format

# Print the tree's inorder traversal as a single line of space-separated values.

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

# 1 2 3 4 5 6 

# Explanation

# The tree's inorder traversal results in 1 2 3 4 5 6 as the required result.

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
            curr = self.root

            while True:
                if val < curr.info:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(val)
                        break
                elif val > curr.info:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(val)
                        break
                else:
                    break

def inOrder(root):
    key = root

    if key == None:
        return
    
    inOrder(key.left)
    print(key.info, end = ' ')
    inOrder(key.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

inOrder(tree.root)