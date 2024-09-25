'''
# Palindrome Linked List

Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.

Examples:

Input: LinkedList: 1->2->1->1->2->1
Output: true
Explanation: The given linked list is 1->2->1->1->2->1 , which is a palindrome and Hence, the output is true.

Input: LinkedList: 1->2->3->4
Output: false
Explanation: The given linked list is 1->2->3->4, which is not a palindrome and Hence, the output is false.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1) 
Note: You should not use the recursive stack space as well

'''


# Linked List Node Creation Class
class ListNode:
    def __init__(self, val=0):
        self.data = val
        self.next = None


# Print Linked List
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
    

# Helper function to create linked lists from arrays
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head
    
    
    
def reverse_linkList(head2):
    prev = None
    curr = head2
    nnext = None

    while curr is not None:
        nnext = curr.next
        curr.next = prev
        prev = curr
        curr = nnext
    
    return prev
    
    
    
def isPalindrome(head):
    #code here
    # Method - I
    # curr = head
    # tail = reverse_linkList(head)
    
    # while curr:
    #     if curr.data != tail.data:
    #         return False
    #     curr = curr.next
    #     tail = tail.next
    
    
    # Method - II 
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    rev = reverse_linkList(slow)
    while rev:
        if head.data != rev.data:
            return False
        head = head.next
        rev = rev.next
    return True
        

   
    
if __name__ == "__main__":
    head = create_linked_list([1,2,1,1,2,1])
    print("Print the given linked list: ")
    print_linked_list(head)
    res = isPalindrome(head)
    print("Given linked list is palindrome or not: ", res)
