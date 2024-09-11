"""
# Middle of a Linked List

Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3.
If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

Examples:

Input: Linked list: 1->2->3->4->5
Output: 3

Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.
Input: Linked list: 2->4->6->7->5->1
Output: 7 

Explanation: The given linked list is 2->4->6->7->5->1 and its middle is 7


"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


import math

def findMid(head1):
    values = []
    while head1:
        values.append(head1.val)
        head1=head1.next
    l = len(values)
    return values[l//2 if l%2==0 else math.floor(l/2)]
    
    


def findMid_slowPtr(head2):
    fast, slow = head2, head2
        
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    if fast.next:
        slow = slow.next
    
    return slow.val

    

if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    print("Linked list:")
    print_linked_list(head)
    
    midNode = findMid(head)
    
    print("Mid Node of the Linked List", midNode)
    print("Mid Node of the Linked List", findMid_slowPtr(head))
    
    
    
    
  
