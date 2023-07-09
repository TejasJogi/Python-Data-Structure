# Given a pointer to the head of a singly-linked list, print each data value from the reversed list. If the given list is empty, do not print anything.

# Example

# head* refers to the linked list with data values 1 -> 2 -> 3 -> Null 

# Print the following:

# 3
# 2
# 1

# Function Description

# Complete the reversePrint function in the editor below.

# reversePrint has the following parameters:

# SinglyLinkedListNode pointer head: a reference to the head of the list

# Prints

# The data values of each node in the reversed list.

# Input Format

# The first line of input contains t, the number of test cases.

# The input of each test case is as follows:

# The first line contains an integer n, the number of elements in the list.
# Each of the next n lines contains a data element for a list node.

# Sample Input

# 3
# 5
# 16
# 12
# 4
# 2
# 5
# 3
# 7
# 3
# 9
# 5
# 5
# 1
# 18
# 3
# 13

# Sample Output

# 5
# 2
# 4
# 12
# 16
# 9
# 3
# 7
# 13
# 3
# 18
# 1
# 5


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
            self.head = node
        else:
            self.tail = node
        self.tail = node
        print(self.tail.data)

def reversePrint(llist):
    # Write your code here
    itr = llist
    
    if itr == None:
        return
    reversePrint(itr.next)
    print(itr.data)

tests = int(input())

for tests_itr in range(tests):
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)