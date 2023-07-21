# head refers to the list of nodes 1 -> 2 -> 3 -> NULL 

# The numbers shown are the node numbers, not their data values. There is no cycle in this list so return 0.

# head refers to the list of nodes 1 -> 2 -> 3 -> 1 -> NULL

# There is a cycle where node 3 points back to node 1, so return 1.

# Function Description

# Complete the has_cycle function in the editor below.

# It has the following parameter:

# SinglyLinkedListNode pointer head: a reference to the head of the list

# Returns

# int: 1 if there is a cycle or 0 if there is not
# Note: If the list is empty,  will be null.

# Input Format

# The code stub reads from stdin and passes the appropriate argument to your function. The custom test cases format will not be described for this question due to its complexity. Expand the section for the main function and review the code if you would like to figure out how to create a custom case.

# Sample Input

# References to each of the following linked lists are passed as arguments to your function:

# Sample Inputs

# 2
# 1
# 1
# 4
# 1
# 2
# 3
# 2

# Sample Output

# 0
# 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None