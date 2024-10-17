"""
# Split Linked List Alternatingly

Given a singly linked list's head. Your task is to complete the function alternatingSplitList()
that splits the given linked list into two smaller lists. The sublists should be made from 
alternating elements from the original list.

Note: 

The sublist should be in the order with respect to the original list.
Your have to return an array containing the both sub-linked lists.
Examples:

Input: LinkedList = 0->1->0->1->0->1
Output: 0->0->0 , 1->1->1
Explanation: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
        

def alternatingSplitList(head):
    #Your code here
    head1 = head
    head2 = head.next
    curr1 = head1
    curr2 = head2
    
    while curr2 != None and curr2.next != None:
        next1 = curr2.next
        next2 = next1.next
        curr1.next = next1
        curr2.next = next2
        curr1 = next1
        curr2 = next2
    
    curr1.next = None
        
    return [head1, head2]



def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



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
    
 
    
    head1, head2 = alternatingSplitList(head)
    
    print("Linked list after spliting linked lists alternate nodes:")
    print_linked_list(head1)
    print_linked_list(head2)
