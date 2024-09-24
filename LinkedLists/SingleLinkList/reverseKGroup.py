"""
# 25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes 
is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        self.random = None

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
def reverse(subHead, k):
    curr = subHead
    prev, nnext = None, None

    while k > 0:
        nnext = curr.next
        curr.next = prev
        prev = curr
        curr = nnext
        k -= 1
    return prev, curr


def reverseKGroup(head, k):
    
    dummy = Node(123)
    dummy.next = head
    temp = dummy

    while temp:
        tracker = temp
        count = k
        while count:
            if tracker == None:
                break
            tracker = tracker.next
            count -= 1
        if tracker == None:
            break
        start, tail = reverse(temp.next, k)
        lastNodeOfReversedGroup = temp.next
        lastNodeOfReversedGroup.next = tail
        temp.next = start
        temp = lastNodeOfReversedGroup
    return dummy.next
        
        
if __name__ == "__main__":

    # Creating a linked list with a loop
    head = Node(2)
    node2 = Node(4)
    node3 = Node(7)
    node4 = Node(8)
    node5 = Node(9)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    
    print("LinkedList: \n")
    print_linked_list(head)
    
    k = 2
    res = reverseKGroup(head, k)
    
    print("LinkedList: \n")
    print_linked_list(res)
    
