# This is an to practice traversing a linked list. Given a pointer to the head node of a linked list, print each node's data element, one per line. If the head pointer is null (indicating the list is empty), there is nothing to print.

# Function Description

# Complete the printLinkedList function in the editor below.

# printLinkedList has the following parameter(s):

# SinglyLinkedListNode head: a reference to the head of the list

# Print

# For each node, print its data value on a new line (console.log in Javascript).

# Input Format

# The first line of input contains n, the number of elements in the linked list.
# The next n lines contain one element each, the data values for each node.

# Note: Do not read any input from stdin/console. Complete the printLinkedList function in the editor below.

# Sample Input

# 2
# 16
# 13

# Sample Output

# 16
# 13



def printLinkedList(head):
    curr = head

    while curr:
        print(curr.data)
        curr = curr.next



llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

printLinkedList(llist.head)