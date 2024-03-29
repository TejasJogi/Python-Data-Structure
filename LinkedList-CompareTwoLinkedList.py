# You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. If all data attributes are equal and the lists are the same length, return 1. Otherwise, return 0.

# The two lists have equal data attributes for the first 3 nodes. list2 is longer, though, so the lists are not equal. Return 0.

# Function Description

# Complete the compare_lists function in the editor below.

# compare_lists has the following parameters:

# SinglyLinkedListNode llist1: a reference to the head of a list
# SinglyLinkedListNode llist2: a reference to the head of a list
# Returns

# int: return 1 if the lists are equal, or 0 otherwise

# The first line contains an integer t, the number of test cases.

# Each of the test cases has the following format:

# The first line contains an integer n, the number of nodes in the first linked list.
# Each of the next n lines contains an integer, each a value for a data attribute.
# The next line contains an integer m, the number of nodes in the second linked list.
# Each of the next m lines contains an integer, each a value for a data attribute.

# Output Format

# Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.

# The output is handled by the code in the editor and it is as follows:

# For each test case, in a new line, print 1 if the two lists are equal, else print 0.

# Sample Input

# 2
# 2
# 1
# 2
# 1
# 1
# 2
# 1
# 2
# 2
# 1
# 2

# Sample Output

# 0


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

def compare_lists(llist1, llist2):

    while llist1 and llist2:
        if llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        else:
            return 0
    
    
    if llist1 == None:
        return 1 if llist2 == None else 0
    if llist2 == None:
        return 0

tests = int(input())

for tests_itr in range(tests):
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

    result = compare_lists(llist1.head, llist2.head)

    print(result)