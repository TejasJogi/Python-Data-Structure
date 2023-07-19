# Given a pointer to the head of a linked list and a specific position, determine the data value at that position. Count backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on.

# Example
# head refers to 3 -> 2 -> 1 -> 0 -> NULL
# positionFromTail = 2

# Each of the data values matches its distance from the tail. The value 2 is at the desired position.

# Function Description

# Complete the getNode function in the editor below.

# getNode has the following parameters:

# SinglyLinkedListNode pointer head: refers to the head of the list
# int positionFromTail: the item to retrieve
# Returns

# int: the value at the desired position
# Input Format

# The first line contains an integer t, the number of test cases.

# Each test case has the following format:
# The first line contains an integer n, the number of elements in the linked list.
# The next n lines contains an integer, the data value for an element of the linked list.
# The last line contains an integer positionFromTail, the position from the tail to retrieve the value of.

# Sample Input

# 2
# 1
# 1
# 0
# 3
# 3
# 2
# 1
# 2

# Sample Output

# 1
# 3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

tests = int(input())

for tests_itr in range(tests):
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    result = getNode(llist.head, position)

    print(str(result) + '\n')