""" 
Reverse a circular link list.
"""

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def print_linked_list(head):
    if head is None:
        print("empty")
        return

    temp = head
    while True:
        print(temp.val, end=" ")
        temp = temp.next
        if temp == head:
            # print(temp.val) # To check if it's a circular linked list
            break
    print()
    

def reverse_linkList(head):
    if head is None:
        return None
    prev = None
    curr = head
    nnext = head

    while curr.next != head:
        nnext = curr.next
        curr.next = prev
        prev = curr
        curr = nnext
    curr.next = prev
    head.next = curr
    return curr


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
    node5.next = head
    print("Linked list:")
    print_linked_list(head)
    

    rev_head = reverse_linkList(head)
    
    print("Linked list after reversed:")
    print_linked_list(rev_head)
    
    
  
