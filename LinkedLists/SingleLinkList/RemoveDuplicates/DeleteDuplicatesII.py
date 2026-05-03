'''
# 82. Remove Duplicates From sorted list II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct 
numbers from the original list. Return the linked list sorted as well.
 

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

        
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        if not head.next:
            return head
        dummy = ListNode(-123, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                temp = curr.val
                while curr and curr.val == temp:
                    curr = curr.next
                prev.next = curr                
            else:
                prev = curr
                curr = curr.next

        return dummy.next

if __name__ == "__main__":
    # Creating a linked list with a loop
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(3)
    node.next.next.next.next = ListNode(3)
    node.next.next.next.next.next = ListNode(5)
    
    print_linked_list(node)
    
    res = Solution().deleteDuplicates(node)
    
    print_linked_list(res)
