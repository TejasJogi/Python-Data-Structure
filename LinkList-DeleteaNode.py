# Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.

# Example

# llist = 0 -> 1 -> 2 -> 3
# position = 2

# After removing the node at position 2, llist' = 0 -> 1 -> 2 -> 3.

# Function Description

# Complete the deleteNode function in the editor below.

# deleteNode has the following parameters:
# - SinglyLinkedListNode pointer llist: a reference to the head node in the list
# - int position: the position of the node to remove

# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the modified list

# Input Format

# The first line of input contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the node data values in order.
# The last line contains an integer, , the position of the node to delete.

# Constraints

# Sample Input

# 8
# 20
# 6
# 2
# 19
# 7
# 4
# 15
# 9
# 3

# Sample Output

# 20 6 2 7 4 15 9


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self,):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        
        self.tail = node

def print_singly_linked_list(data):
    itr = data

    while itr:
        print(itr.data)
        itr = itr.next

def deleteNode(llist, position):
    if position == 0:
        return llist.next
    itr = llist
    for i in range(position-1):
        itr = itr.next
    itr.next = itr.next.next
    
    return llist


llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

position = int(input())

llist1 = deleteNode(llist.head, position)

print_singly_linked_list(llist1)