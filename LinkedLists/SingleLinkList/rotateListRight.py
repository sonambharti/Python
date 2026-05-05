"""
# 61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]


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


class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        if not head.next:
            return head

        dummy_head = head
        tail = head
        
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        
        k = k % n
        if k == 0:
            return head
            
        rem = n - k - 1
    
        while rem > 0:
            dummy_head = dummy_head.next
            rem -= 1
            
        temp_head = dummy_head.next
        tail.next = head
        dummy_head.next = None
        
        return temp_head
            


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
    node5.next = None
    print("Linked list:")
    print_linked_list(head)
    
    rotated_list = Solution().rotateRight(head, 2)
    print_linked_list(rotated_list)
    
    
  
