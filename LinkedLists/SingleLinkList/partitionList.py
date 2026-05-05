"""
# 86.Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x 
come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def create_link_list(arr):
    n = len(arr)
    head = ListNode(arr[0])
    dummy_head = head
    
    for i in range(1, n):
        dummy_head.next = ListNode(arr[i])
        dummy_head = dummy_head.next
    return head
    
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
        
class Solution:
    def partitionList(self, head, x):
        dummy = ListNode(-123, head)
        first = dummy
        sec = ListNode(-123)
        
        temp = sec
        
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                sec.next = head
                sec = sec.next
            head = head.next
            
        first.next = temp.next
        sec.next = None
        return dummy.next
        
    

if __name__ == "__main__":
    # Helper function to print the linked list
    arr = [1,7,5,1,9,2,5,1]
    
    head = create_link_list(arr)
    
    print("Linked list:")
    print_linked_list(head)
    
    largerNodeList = Solution().partitionList(head, 5)
    print_linked_list(largerNodeList)
    
    
  
