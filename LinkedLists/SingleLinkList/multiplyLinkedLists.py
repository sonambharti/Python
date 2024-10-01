"""
# Multiply 2 Linnked Lists

Given elements as nodes of the two singly linked lists. The task is to multiply these 
two linked lists, say L1 and L2.

Note: The output could be large take modulo 109+7.

Examples :

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation: 

Multiplication of 32 and 2 gives 64.
Input: LinkedList L1: 1->0->0 , LinkedList L2 : 1->0
Output: 1000
Explanation: 

Multiplication of 100 and 10 gives 1000.
Expected Time Complexity: O(max(n,m))
Expected Auxilliary Space: O(1)
where n is the size of L1 and m is the size of L2

"""
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
    
def multiplyLL(head, head1):
    num1, num2 = 0, 0
    temp, temp1 = head, head1
    
    while temp:
        num1 = num1*10 + temp.data
        temp = temp.next
    
    while temp1:
        num2 = num2*10 + temp1.data
        temp1 = temp1.next
    
    res = (num1 * num2) % (10**9+7)
    res = str(res)
    res = res.split()
    res = [int(x) for x in res]
    res_head = create_linked_list(res)
    return res_head
        
    
    
if __name__ == "__main__":
    head = create_linked_list([1,2,3])
    head1 = create_linked_list([3, 0])
    print("Print the given linked list1: ")
    print_linked_list(head)
    print("Print the given linked list2: ")
    print_linked_list(head1)
    
    ans = multiplyLL(head, head1)
    print("The resultant linked list: ")
    print_linked_list(ans)
    
    
    
    
