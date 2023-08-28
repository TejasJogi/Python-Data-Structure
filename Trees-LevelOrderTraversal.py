# Given a pointer to the root of a binary tree, you need to print the level order traversal of this tree. In level-order traversal, nodes are visited level by level from left to right. Complete the function levelOrder and print the values in a single line separated by a space.

# For example:

#      1
#       \
#        2
#         \
#          5
#         /  \
#        3    6
#         \
#          4  
# For the above tree, the level order traversal is 1 -> 2 -> 5 -> 3 -> 6 -> 4.

# Input Format

# You are given a function,

# void levelOrder(Node * root) {

# } 

# Output Format

# Print the values in a single line separated by a space.

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

# 1 2 5 3 6 4

# Explanation

# We need to print the nodes level by level. We process each level from left to right.
# Level Order Traversal: 1 -> 2 -> 5 -> 3 -> 6 -> 4.

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

from collections import deque

def levelOrder(root):
    #Write your code here
    if root == None:
        return
    
    que = deque()
    que.append(root)

    while que:
        val = que.popleft()
        print(val.info, end = ' ')

        if val.left:
            que.append(val.left)
        
        if val.right:
            que.append(val.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)