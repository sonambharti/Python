'''
# 83. Delete Duplicates From sorted list

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

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
        nextn = head.next

        while nextn:
            if curr.val == nextn.val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
            nextn = nextn.next

        return dummy.next

if __name__ == "__main__":
    # Creating a linked list with a loop
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    
    print_linked_list(node)
    
    res = Solution().deleteDuplicates(node)
    
    print_linked_list(res)
