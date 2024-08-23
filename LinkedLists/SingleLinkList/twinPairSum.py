"""
# 2130. Maximum twin sum of a linked list

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list 
is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. 
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

"""

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        


def getMiddle(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
    
    
    
def reverse(midHalf):
    prev = None
    curr = midHalf
    nnext = None

    while curr is not None:
        nnext = curr.next
        curr.next = prev
        prev = curr
        curr = nnext
    
    return prev
    
    
    
def pairSum(head):
        
        maxVal = 0

        midNode = getMiddle(head)
        revSecHalf = reverse(midNode)

        while revSecHalf:
            maxVal = max(maxVal, head.val + revSecHalf.val)
            revSecHalf = revSecHalf.next
            head = head.next

        return maxVal
        
        

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(7)
    node4 = ListNode(8)
    node5 = ListNode(9)
    node6 = ListNode(6)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = None
    
    print("Linked list:")
    print_linked_list(head)
    
    result = pairSum(head)
    
    print("Maximum sum of Linked List using pair sum = ", result)
   
  
