'''
#   Sort a linked list of 0s, 1s and 2s

Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange 
the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

Examples:

Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2

Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2

Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, 
and 1s in between.

Input: head = 2 → 2 → 0 → 1

Output: 0 → 1 → 2 → 2

Explanation: After arranging all the 0s, 1s and 2s in the given format, the output will be 0 → 1 → 2 → 2.
'''

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
    def segregate(self, head):
        #code here
        zero = ListNode(1231)
        one = ListNode(1232)
        two = ListNode(1233)
        res = zero
        temp1 = one
        temp2 = two
        
        while head:
            v = head.val
            if v == 0:
                zero.next = head
                zero = zero.next
            elif v == 1:
                one.next = head
                one = one.next
            else:
                two.next = head
                two = two.next
            head = head.next
        one.next = temp2.next
        zero.next = temp1.next
        two.next = None
        
        return res.next
        

if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head = ListNode(1)
    node2 = ListNode(0)
    node3 = ListNode(0)
    node4 = ListNode(2)
    node5 = ListNode(1)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    print("Linked list:")
    print_linked_list(head)
    
    obj = Solution()
    res_head = obj.segregate(head)
    print("Linked list after sorting:")
    print_linked_list(res_head)
    
  
