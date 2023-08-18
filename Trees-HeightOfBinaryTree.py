# The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height 2:

# Function Description

# Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

# getHeight or height has the following parameter(s):

# root: a reference to the root of a binary tree.

# Note -The Height of binary tree with single node is taken as zero.

# Input Format

# The first line contains an integer n, the number of nodes in the tree.
# Next line contains n space separated integer where ith integer denotes node[i].data.

# Note: Node values are inserted into a binary search tree before a reference to the tree's root node is passed to your function. In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value.

# Output Format

# Your function should return a single integer denoting the height of the binary tree.

# Sample Input

# 7
# 4 2 1 3 7 6 5

# Sample Output

# 3

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree():    
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

def height(root):
    key = root

    lheight = 0
    rheight = 0

    if key.left:
        lheight = height(key.left) + 1
    
    if key.right:
        rheight = height(key.right) + 1

    if lheight > rheight:
        return lheight
    else:
        return rheight


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))