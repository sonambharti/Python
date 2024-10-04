""" 
Implement a circular link list and add nodes at it's head and to it's tail.

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
            break
    print()


def insertAtHead(head, val):
    n = ListNode(val)
    if not head:
        n.next = n
        head = n
        return
    
    temp = head
    
    while temp.next != head:
        temp = temp.next
        
    temp.next = n
    n.next = head
    head = n
    return head


def insertAtTail(head, val):
    if not head:
        insertAtHead(head, val)
        return 
    
    n = ListNode(val)
    temp = head
    
    while temp.next != head:
        temp = temp.next
        
    temp.next = n
    n.next = head
    head = n
    return




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
    
    val1 = 6
    insertAtTail(head, val1)
    print("Linked list after adding node at tail:")
    print_linked_list(head)
    
    val2 = 0
    head = insertAtHead(head, val2)
    print("Linked list after adding node at head:")
    print_linked_list(head)
    
    
  
