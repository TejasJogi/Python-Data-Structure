# Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.

# Example

#  refers to the list 

# Return a reference to the new list: .

# Function Description

# Complete the sortedInsert function in the editor below.

# sortedInsert has two parameters:

# DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list

# int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

# Returns

# DoublyLinkedListNode pointer: a reference to the head of the list
# Note: Recall that an empty list (i.e., where ) and a list with one element are sorted lists.

# Input Format

# The first line contains an integer , the number of test cases.

# Each of the test case is in the following format:

# The first line contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the data for each node of the linked list.
# The last line contains an integer, , which needs to be inserted into the sorted doubly-linked list.

# Constraints

# Sample Input

# STDIN   Function
# -----   --------
# 1       t = 1
# 4       n = 4
# 1       node data values = 1, 3, 4, 10
# 3
# 4
# 10
# 5       data = 5

# Sample Output

# 1 3 4 5 10


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

t = int(input())

for t_itr in range(t):
    llist_count = int(input())

    llist = DoublyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    llist1 = sortedInsert(llist.head, data)

    print_doubly_linked_list(llist1)