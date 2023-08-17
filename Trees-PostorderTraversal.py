# Complete the postOrder function in the editor below. It received 1 parameter: a pointer to the root of a binary tree. It must print the values in the tree's postorder traversal as a single line of space-separated values.

# Input Format

# Our test code passes the root node of a binary tree to the postOrder function. 

# Output Format

# Print the tree's postorder traversal as a single line of space-separated values.

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

# 4 3 6 5 2 1 

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

def postOrder(root):
    #Write your code here
    key = root

    if key is None:
        return
    
    postOrder(key.left)
    postOrder(key.right)
    print(key.info, end=' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)