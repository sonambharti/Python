"""
# 142. LinnkedList Cycle II

Given the head of a linked list, return the node where the cycle begins. If there 
is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer. Internally, pos is used 
to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
"""
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


def findStartingLoopNode(head):
    #Your code here
    slow, fast = head, head
    
    # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
    # until they either meet or the fast pointer reaches the end of the list.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # If the pointers meet, there is a cycle in the linked list.
            # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
            # until they meet again. The node where they meet is the starting point of the cycle.
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    # If the fast pointer reaches the end of the list without meeting the slow pointer,
    # there is no cycle in the linked list. Return None.
    return None
       
        
        
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
    
    res = findStartingLoopNode(head)
    
    print("Starting of the loop:", res.val)
    
    
  
