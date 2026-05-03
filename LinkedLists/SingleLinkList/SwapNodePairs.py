'''
# 24. Swap nodes in pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem 
without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

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


def swapPairs(head):
    flag = False
    dummy = ListNode(-123, head)
    res = dummy
    prev = res
    
    while dummy and head:
        if flag:
            dummy.val, head.val = head.val, dummy.val
        head = head.next
        dummy = dummy.next
        flag = not flag

    return res.next
    

if __name__ == "__main__":
    # Creating a linked list with a loop
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    
    print_linked_list(node)
    
    res = swapPairs(node)
    
    print_linked_list(res)
