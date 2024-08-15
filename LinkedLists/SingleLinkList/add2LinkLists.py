"""
# Add Number Linked Lists

Given two numbers, num1, and num2, represented by linked lists. The task is to return 
the head of the linked list that represents the sum of these two numbers.

For example, the number 190 will be represented by the linked list, 1->9->0->null, 
similarly 25 by 2->5->null. Sum of these two numbers is 190 + 25 = 215, which will be 
represented by 2->1->5->null. You are required to return the head of the linked list 2->1->5->null.

Note: There can be leading zeros in the input lists, but there should not be any leading 
zeros in the output list.

Examples:

Input: num1 = 45 (4->5->null), num2 = 345 (3->4->5->null)
Output:  3->9->0->null  
 
Explanation: 
For the given two linked list (4 5) and (3 4 5), after adding the two linked list resultant 
linked list will be (3 9 0).
Input: num1 = 0063 (0->0->6->3->null), num2 = 07 (0->7->null)
Output: 7->0->null
"""


class ListNode:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        
        
def reverse_linkList(head):
    prev = None
    curr = head
    nnext = None

    while curr is not None:
        nnext = curr.next
        curr.next = prev
        prev = curr
        curr = nnext
    
    return prev
    
def addLists(head1, head2):
    # CODE HERE
    
    l1 = reverse_linkList(head1)
    l2 = reverse_linkList(head2)
    carry = 0
    ans = p = ListNode(123)

    while l1 and l2:
        sum = l1.data + l2.data + carry
        carry = sum//10
        p.next = ListNode(sum%10)
        p = p.next
        l1 = l1.next
        l2 = l2.next

    if l2:
        l1 = l2

    while l1:
        sum = l1.data + carry
        carry = sum//10
        p.next = ListNode(sum%10)
        p = p.next
        l1 = l1.next
    
    if carry:
        p.next = ListNode(carry)

    ans = ans.next
    return reverse_linkList(ans)

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")



if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head1 = ListNode(4)
    node2 = ListNode(9)
    
    head1.next = node2
    node2.next = None
    
    
    
    head2 = ListNode(2)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    
    head2.next = node2_2
    node2_2.next = node2_3
    node2_3.next = None
   
    
    print("Linked list:")
    print_linked_list(head1)
    print_linked_list(head2)
    
    res_head = addLists(head1, head2)
    
    print("Linked list after reversed:")
    print_linked_list(res_head)
    
  
