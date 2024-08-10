"""
Rotate a Linked List

Given the head of a singly linked list, the task is to rotate the linked list 
anti-clockwise by k nodes, i.e., left-shift the linked list by k nodes, where 
k is a given positive integer smaller than or equal to length of the linked list.

Examples:

Input: linkedlist: 2->4->7->8->9 , k = 3
Output: 8->9->2->4->7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
        

def rotate(head, k):
    # code here
    first = head
    last = head
    
    while last.next:
        last = last.next
        
    for i in range(k):
        temp = first
        first = first.next
        temp.next = None
        last.next = temp
        last = last.next
        
    return first



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
    
    k = 3 
    
    res_head = rotate(head, k)
    
    print("Linked list after rotation:")
    print_linked_list(res_head)
    
  
