# You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

# Function Description

# Complete the insertNodeAtTail function in the editor below.

# insertNodeAtTail has the following parameters:

# SinglyLinkedListNode pointer head: a reference to the head of a list
# int data: the data value for the node to insert
# Returns

# SinglyLinkedListNode pointer: reference to the head of the modified linked list

# Input Format

# The first line contains an integer n, the number of elements in the linked list.
# The next n lines contain an integer each, the value that needs to be inserted at tail.

# Sample Input

# STDIN Function ----- -------- 5 size of linked list n = 5 141 linked list data values 141..474 302 164 530 474

# Sample Output

# 141
# 302
# 164
# 530
# 474


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def insertNodeAtTail(head, data):
    node = Node(data)

    if head == None:
        head = node
    else:
        tail = node
    tail = node
    print(tail.data)


llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtTail(llist.head, llist_item)
    llist.head = llist_head

print_singly_linked_list(llist.head)