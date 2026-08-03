"""
# 2074. Reverse Nodes in Even Length Groups

You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the 
natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.


Example 1:

Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.

Example 2:

Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.

Example 3:

Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.
"""

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
    
def reverse(head):
    if not head or not head.next:
        return head
    prev, curr, nnext = None, head, head.next
    while nnext:
        curr.next = prev
        prev = curr
        curr = nnext
        nnext = nnext.next
    curr.next = prev
    return curr
    
class Solution:
    def findLength(self, temp):
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverseEvenLengthGroups(self, head):
        
        size = self.findLength(head)
        
        curr = head
        probableGroupSize = 1
        p = None
        while curr:
            actualGroupSize = min(size, probableGroupSize)
            
            if actualGroupSize % 2 == 0:
                # reverse 
                counter = 0
                prev, curr, nnext = None, curr, None
                temp1 = curr
                while counter < actualGroupSize:
                    counter = counter + 1
                    nnext = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nnext
                p.next = prev
                temp1.next = curr
                p = temp1
            else:
                counter = 0
                while counter < actualGroupSize:
                    counter = counter + 1
                    p = curr
                    curr = curr.next
            
            probableGroupSize += 1
            size = size - actualGroupSize
        return head
                
        
   
        
if __name__ == "__main__":
    arr = [5,2,6,3,9,1,7,3,8,4]
    
    head = createLinkedlist(arr)
    
    print_linked_list(head) # print the Linked list Node
    # rev = reverse(head)
    # print_linked_list(rev)
    
    res = Solution().reverseEvenLengthGroups(head)
    print_linked_list(res)
    
