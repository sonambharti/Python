"""
# Delete alt nodes

Given a Singly Linked List, Delete all alternate nodes of the list ie delete all the nodes
present in even positions.

Examples :

Input: LinkedList: 1->2->3->4->5->6
 
Output: 1->3->5

Explanation: Deleting alternate nodes ie 2, 4, 6 results in the linked list with elements 1->3->5.
Input: LinkedList: 99->59->42->20
 
Output: 99->42
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= number of nodes <= 105
1 <= node->data <= 103
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
        

def deleteAlt(head):
    while head is not None and head.next is not None:
        head.next = head.next.next
        head = head.next



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
    
 
    
    deleteAlt(head)
    
    print("Linked list after Deleting alternate nodes:")
    print_linked_list(head)
    
  
