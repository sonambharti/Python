'''
# 91. Reverse Linklist - II 

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
'''

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def createList(arr):
    n = len(arr)
    head = ListNode(arr[0])
    listNode = head
    
    for i in range(1, n):
        temp = ListNode(arr[i])
        listNode.next = temp
        listNode = listNode.next
    listNode.next = None
    
    return head
    
    
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


class Solution:
    def reverse(self, node, x):
        curr = node
        prev, nnext = None, None

        while x > 0:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext
            x -= 1
            
        return prev, curr

    def reverseBetween(self, head, left, right):
        if not head:
            return None
        tail = head
        prev = None
        n = 0

        while tail:
            tail = tail.next
            n += 1
        
        if n == 1 or left == right:
            return head
            
        temp = head
        for i in range(1, left):
            prev = temp
            temp = temp.next

        revers, nextRight  = self.reverse(temp, right)
        prev.next = revers
        temp.next = nextRight

        return head

if __name__ == "__main__":
    # Creating a linked list with a loop
    arr = [1, 2, 3, 4, 5, 6, 7]
    
    node = createList(arr)
    
    print_linked_list(node)
    obj = Solution()
    res = obj.reverseBetween(node, 2, 4)
    
    print_linked_list(res)
