'''
# 2807. Insert Greatest Common Divisors in Linked List

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]

Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked
list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.


'''


# Linked List Node Creation Class
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Print Linked List
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
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
    
    
    
# def gcd(a, b): # can cause segmentation fault due to recursion limit in python
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     if a == b:
#         return a
#     if a > b:
#         return gcd(a-b, b)
#     return gcd(a, b-a)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


    
    
def insertGreatestCommonDivisors(head):
    if not head and not head.next:
        return head

    prev = head
    temp = head.next   

    while temp:
        data = gcd(prev.val, temp.val)
        newNode = ListNode(data)
        nextPtr = temp.next 
        prev.next = newNode
        newNode.next = temp
        prev = temp
        temp = nextPtr
    return head


    
if __name__ == "__main__":
    head = create_linked_list([18,6,10,3])
    print("Print the given linked list: ")
    print_linked_list(head)
    res = insertGreatestCommonDivisors(head)
    print("Print the resultant linked list: ")
    print_linked_list(res)
