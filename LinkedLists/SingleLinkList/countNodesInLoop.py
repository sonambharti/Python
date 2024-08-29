"""
# Find length of loop

Given the head of a linked list, determine whether the list contains a loop. If a loop 
is present, return the number of nodes in the loop, otherwise return 0.



Note: 'c' is the position of the node which is the next pointer of the last node of the 
linkedlist. If c is 0, then there is no loop.

Examples:

Input: LinkedList: 25->14->19->33->10->21->39->90->58->45, c = 4
Output: 7
Explanation: The loop is from 33 to 45. So length of loop is 33->10->21->39-> 90->58->45 = 7. 
The number 33 is connected to the last node of the linkedlist to form the loop because according 
to the input the 4th node from the beginning(1 based indexing) 
will be connected to the last node for the loop.
 
Input: LinkedList: 5->4, c = 0
Output: 0
Explanation: There is no loop.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
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


def countNodesInLoop(head):
    #Your code here
    def findLoopLength(node):
        count = 1
        curr = node
        while curr.next != node:
            curr = curr.next
            count += 1
        return count
        
        
    def detectLoop(head):
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return findLoopLength(slow)
        return 0
    return detectLoop(head)
        
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
    
    res = countNodesInLoop(head)
    
    print("Length of the loop:", res)
    
    
  
