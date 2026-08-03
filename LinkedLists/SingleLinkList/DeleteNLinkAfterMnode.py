"""
# Delete N After Every M in a Linked List

Given a linked list, delete n nodes after skipping m nodes of a linked list until the last of the linked list.

Examples:

Input: head: 9 -> 1 -> 3 -> 5 -> 9 -> 4 -> 10 -> 1, n = 1, m = 2
Output: 9 -> 1 -> 5 -> 9 -> 10 -> 1
Explanation: Deleting 1 node after skipping 2 nodes each time, we have list as 9 -> 1 -> 5 -> 9 -> 10 -> 1.

Input: head: 1 -> 2 -> 3 -> 4 -> 5 -> 6, n = 1, m = 6
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Explanation: After skipping 6 nodes for the first time , we will reach of end of the linked list, so, we will get
the given linked list itself.
"""
class LinkedlistNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
def createLinkedlist(arr):
    ll = LinkedlistNode(-123)
    temp = ll
    for el in arr:
        node = LinkedlistNode(el)
        temp.next = node
        temp = temp.next
    temp.next = None
    return ll.next
    
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    

class Solution:
    def linkDelete(self, head, n, m):
        # Code here
        if n == 0:
            return head
        tempNode = head
        
        while tempNode:
            i, j = m-1, n
            while i>0 and tempNode:
                tempNode = tempNode.next
                i -= 1
            if tempNode is None:
                break
            mid = tempNode
            tempNode = tempNode.next
            while j>0 and tempNode:
                tempNode = tempNode.next
                j -= 1
            mid.next = tempNode
        return head
        
        
        
if __name__ == "__main__":
    # head: 9 -> 1 -> 3 -> 5 -> 9 -> 4 -> 10 -> 1, n = 1, m = 2
    arr = [9,1,3,5,9,4,10,1]
    n = 1 
    m = 2
    
    head = createLinkedlist(arr)
    
    print_linked_list(head) # print the Linked list Node
    
    res = Solution().linkDelete(head, n, m)
    print_linked_list(res)
    
