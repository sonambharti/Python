"""
# Reverse a Linked List

Given the head of a singly linked list, the task is to reverse the linked list.

Examples:

Input: linkedlist: 2->4->7->8->9 
Output: 9->8->7->4->2


"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
        

def reverse(head):
    # code here
    if not head or not head.next:
        return head
        
    prev, curr, nextn = head, head.next, head.next.next
    
    while nextn:
        curr.next = prev
        prev = curr
        curr = nextn
        nextn = nextn.next
        
    head.next=None
    curr.next=prev    
        
    return curr



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
    
    res_head = reverse(head)
    
    print("Linked list after reversed:")
    print_linked_list(res_head)
    
  
