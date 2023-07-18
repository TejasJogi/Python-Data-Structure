# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

# Example
# headA refers to 1 -> 3 -> 7 -> Null 
# HeadB refers to 1 -> 2 -> Null

# The new list is 1 -> 1 -> 2 -> 3 -> 7 -> Null

# Function Description

# Complete the mergeLists function in the editor below.

# mergeLists has the following parameters:

# SinglyLinkedListNode pointer headA: a reference to the head of a list
# SinglyLinkedListNode pointer headB: a reference to the head of a list

# Returns

# SinglyLinkedListNode pointer: a reference to the head of the merged list

# Input Format

# The first line contains an integer t, the number of test cases.

# The format for each test case is as follows:

# The first line contains an integer n, the length of the first linked list.
# The next n lines contain an integer each, the elements of the linked list.
# The next line contains an integer m, the length of the second linked list.
# The next m lines contain an integer each, the elements of the second linked list.

# Sample Input

# 1
# 3
# 1
# 2
# 3
# 2
# 3
# 4

# Sample Output

# 1 2 3 3 4 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
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

def print_singly_linked_list(head):
    itr = head

    while itr:
        print(str(itr.data))

        itr = itr.next

def mergeLists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    itr = head
    while head1 != None or head2 != None:
        if head1 == None:
            itr.next = head2
            break
        if head2 == None:
            itr.next = head1
            break
        if head1.data <= head2.data:
            itr.next = head1
            head1 = head1.next
        else:
            itr.next = head2
            head2 = head2.next
        
        itr = itr.next

    return head

if __name__ == '__main__':

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

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3)