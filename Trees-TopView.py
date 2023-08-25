# Given a pointer to the root of a binary tree, print the top view of the binary tree.

# The tree as seen from the top the nodes, is called the top view of the tree.

# For example :

#    1
#     \
#      2
#       \
#        5
#       /  \
#      3    6
#       \
#        4

# Top View : 1 -> 2 -> 5 -> 6

# Complete the function  and print the resulting values on a single line separated by space.

# Input Format

# You are given a function,

# void topView(node * root) {

# }

# Output Format

# Print the values on a single line separated by space.

# Sample Input

#    1
#     \
#      2
#       \
#        5
#       /  \
#      3    6
#       \
#        4

# Sample Output

# 1 2 5 6

# Explanation

#    1
#     \
#      2
#       \
#        5
#       /  \
#      3    6
#       \
#        4

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

def topview(root):
    #Write your code here
    hm={}
    queue=[]
    queue.append((root,0))
    while(queue):
        q=queue.pop(0)
        if q[1] not in hm:
            hm[q[1]]=q[0].info
        if q[0].left:
            queue.append((q[0].left,q[1]-1))
        if q[0].right:
            queue.append((q[0].right,q[1]+1))
    for k, v in sorted(hm.items()):
        print(str(v)+' ', end='')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)