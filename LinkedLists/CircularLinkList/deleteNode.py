""" 
Delete a node from a circular link list.
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
            # print(temp.val)
            break
    print()
    

def deleteNode(head, key):
    if head is None:
        return head
    # If the list contains only one node
    if head.val == key and head.next == head:
        return None
    
    # Case 1: If the node to be deleted is the head
    if head.val == key:
        # Find the last node to update its next pointer to the new head
        temp = head
        while temp.next != head:
            temp = temp.next
        # Point last node to the new head (head.next)
        temp.next = head.next
        # Update the head to the new head (head.next)
        head = head.next
        return head

    # Case 2: If the node to be deleted is not the head
    prev = None
    temp = head
    while temp.next != head:
        if temp.val == key:
            prev.next = temp.next
            return head
        prev = temp
        temp = temp.next

    # Special case: If the node to be deleted is the last node
    if temp.val == key:
        prev.next = temp.next

    return head
        

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
    

    key = 2
    head = deleteNode(head, key)
    print("Linked list after deleting node:")
    print_linked_list(head)
    
    key = 1
    head = deleteNode(head, key)
    print("Linked list after deleting node:")
    print_linked_list(head)
    
    
    
  
