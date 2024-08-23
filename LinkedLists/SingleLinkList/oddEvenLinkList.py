"""
# 328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed 
by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the 
input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
        

def oddEvenList(head):
    if (not head or not head.next or not head.next.next):
        return head
    odd = head
    even = head.next
    even_head = even 

    while even  and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = even_head
    # fast.next = None

    return head



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
    
 
    
    res_head = oddEvenList(head)
    
    print("Linked list after rotation:")
    print_linked_list(res_head)
    
  
