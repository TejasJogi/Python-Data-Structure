# You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.

# Example

# head refers to the first node in the list 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 3 -> NULL.

# Remove 1 of the 2 data values and return head pointing to the revised list 1 -> 2 -> 3 -> NULL.

# Function Description

# Complete the removeDuplicates function in the editor below.

# removeDuplicates has the following parameter:

# SinglyLinkedListNode pointer head: a reference to the head of the list

# Returns

# SinglyLinkedListNode pointer: a reference to the head of the revised list

# Input Format

# The first line contains an integer t, the number of test cases.

# The format for each test case is as follows:

# The first line contains an integer n, the number of elements in the linked list.
# Each of the next n lines contains an integer, the data value for each of the elements of the linked list.

# Sample Input

# STDIN   Function
# -----   --------
# 1       t = 1
# 5       n = 5
# 1       data values = 1, 2, 2, 3, 4
# 2
# 2
# 3
# 4

# Sample Output

# 1 2 3 4 

t = int(input())

for t_itr in range(t):
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    llist1 = removeDuplicates(llist.head)

    print_singly_linked_list(llist1, ' ')