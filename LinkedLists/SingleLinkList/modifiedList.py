"""
# 3217. Delete Nodes From Linked List Present in Array

You are given an array of integers nums and the head of a linked list. Return the
head of the modified linked list after removing all nodes from the linked list
that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]


"""


class ListNode:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        
        

def modifiedList(nums, head):
    d = ListNode(-1)
    t = d
    s = set(nums)
    
    while head:
        if head.data not in s :
            t.next = head
            t = t.next
        head = head.next
    t.next = None
    return d.next
        


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
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
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    
    print("Linked list:")
    print_linked_list(head)
    
    nums = [1,2,3]
    
    res_head = modifiedList(nums, head)
    
    print("Linked list after modification:")
    print_linked_list(res_head)
    
  
