# Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

# Note: The head node might be NULL to indicate that the list is empty.

# Function Description

# Complete the reverse function in the editor below.

# reverse has the following parameter(s):

# DoublyLinkedListNode head: a reference to the head of a DoublyLinkedList
# Returns
# - DoublyLinkedListNode: a reference to the head of the reversed list

# Input Format

# The first line contains an integer , the number of test cases.

# Each test case is of the following format:

# The first line contains an integer , the number of elements in the linked list.
# The next  lines contain an integer each denoting an element of the linked list.

# Output Format

# Return a reference to the head of your reversed list. The provided code will print the reverse array as a one line of space-separated integers for each test case.

# Sample Input

# 1
# 4
# 1
# 2
# 3
# 4

# Sample Output

# 4 3 2 1 

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

def print_doubly_linked_list(head):

    curr = head
    while curr is not None:
        print(curr.data, end = ' ')
        curr = curr.next

t = int(input())

for t_itr in range(t):
    llist_count = int(input())

    llist = DoublyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    llist1 = reverse(llist.head)

    print_doubly_linked_list(llist1)