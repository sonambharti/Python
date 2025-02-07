'''
# Merge two sorted linked lists

Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both 
lists and return the head of the sorted merged list.

Examples:

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40

Input: head1 = 1 -> 1, head2 = 2 -> 4
Output: 1 -> 1 -> 2 -> 4
'''


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


def sortedMerge(head1, head2):
    # code here
    temp = ListNode(123)
    res = temp
    
    while head1 and head2:
        if head1.val <= head2.val:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
    
    while head1:
        temp.next = head1
        temp = temp.next
        head1 = head1.next
    
    while head2:
        temp.next = head2
        temp = temp.next
        head2 = head2.next
    
    return res.next
    


if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head1 = ListNode(5)
    node2 = ListNode(10)
    node3 = ListNode(15)
    node4 = ListNode(40)
    
    
    head1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    
    print("Linked list 1:")
    print_linked_list(head1)
    
    
    head2 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(20)
   
    
    head2.next = node2
    node2.next = node3
    node3.next = None
    
    print("Linked list 2:")
    print_linked_list(head2)
    
    res = sortedMerge(head1, head2)
    print("Merged Link list: ")
    print_linked_list(res)
    
    
    
    
