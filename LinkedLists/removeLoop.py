"""
Your task is to complete the function removeLoop() which takes the head of the linked list as the input parameter. 
Simply remove the loop in the list (if present) without disconnecting any nodes from the list.

"""
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
def removeLoop(head):
    # code here
    # remove the loop without losing any nodes
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        prev = fast.next
        fast = fast.next.next

        if slow == fast:
            print("Loop")
            slow = head
            
            while slow != fast:
                fast = fast.next
                slow = slow.next
                prev = prev.next
        
            # Now fast points to the last node of the loop, make its next None to remove the loop
            prev.next = None
            return
    print("Loop Not found")

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

        
if __name__ == "__main__":
    # Helper function to print the linked list
    
    # Example usage:
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
    node5.next = node3  # Creating a loop
    # node5.next = None
    # print("Linked list before removing the loop:")
    # print_linked_list(head)
    
    removeLoop(head)
    
    print("Linked list after removing the loop:")
    print_linked_list(head)
    
  
