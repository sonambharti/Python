'''
# Find the Sum of Last N nodes of the Linked List

Given a single linked list, calculate the sum of the last n nodes.

Note: It is guaranteed that n <= number of nodes.

Examples:

Input: Linked List: 5->9->6->3->4->10, n = 3

Output: 17
Explanation: The sum of the last three nodes in the linked list is 3 + 4 + 10 = 17.
Input: Linked List: 1->2, n = 2

Output: 3
Explanation: The sum of the last two nodes in the linked list is 2 + 1 = 3.
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
    
    
def sumOfLastN_Nodes(head, n):
    #function should return sum of last n nodes
    temp = head
    summ = 0
    list_size = 0
    
    while temp:
        list_size += 1
        temp = temp.next
        
    
    while list_size > n:
        list_size -= 1
        head = head.next
    
    while head:
        summ += head.data
        head = head.next
    
    return summ  
   
    
if __name__ == "__main__":
    head = create_linked_list([1,2,1,1,2,1])
    print("Print the given linked list: ")
    print_linked_list(head)
    n = 3
    res = sumOfLastN_Nodes(head, n)
    print(f"The sum of last {n} nodes: ", res)
