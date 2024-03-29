# Given pointers to the head nodes of 2 linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's data value.

# Note: After the merge point, both lists will share the same node pointers.

# Example

# In the diagram below, the two lists converge at Node x:

# [List #1] a--->b--->c
#                      \
#                       x--->y--->z--->NULL
#                      /
#      [List #2] p--->q
      
# Function Description

# Complete the findMergeNode function in the editor below.

# findMergeNode has the following parameters:

# SinglyLinkedListNode pointer head1: a reference to the head of the first list
# SinglyLinkedListNode pointer head2: a reference to the head of the second list

# Returns

# int: the data value of the node where the lists merge
# Input Format

# Do not read any input from stdin/console.

# The first line contains an integer t, the number of test cases.

# Each of the test cases is in the following format:
# The first line contains an integer, index, the node number where the merge will occur.
# The next line contains an integer, list1count that is the number of nodes in the first list.
# Each of the following list1count lines contains a data value for a node. The next line contains an integer, list2count that is the number of nodes in the second list.
# Each of the following list2count lines contains a data value for a node.

# Constraints

# The lists will merge.
# head1, head2 != null.
# head1 != head2.

# Sample Input

# The diagrams below are graphical representations of the lists that input nodes head1 and head2 are connected to.

# Test Case 0

#  1
#   \
#    2--->3--->NULL
#   /
#  1

# Test Case 1

# 1--->2
#       \
#        3--->Null
#       /
#      1

# Sample Output

# 2
# 3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self,data):
        node = Node(data)

        if self.head == None:
            self.head == node
        else:
            self.tail.next = node
        
        self.tail = node

def findMergeNode(head1, head2):
    while head1:
        node = head2
        while node:
            if head1 == node:
                return head1.data
            node = node.next
        head1 = head1.next

tests = int(input())

for tests_itr in range(tests):
    index = int(input())

    llist1_count = int(input())

    llist1 = SinglyLinkedList()

    for _ in range(llist1_count):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)
        
    llist2_count = int(input())

    llist2 = SinglyLinkedList()

    for _ in range(llist2_count):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)
        
    ptr1 = llist1.head;
    ptr2 = llist2.head;

    for i in range(llist1_count):
        if i < index:
            ptr1 = ptr1.next
            
    for i in range(llist2_count):
        if i != llist2_count-1:
            ptr2 = ptr2.next

    ptr2.next = ptr1

    result = findMergeNode(llist1.head, llist2.head)

    print(str(result) + '\n')