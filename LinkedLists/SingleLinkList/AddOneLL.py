"""
# Add 1 to a Linked List

GYou are given a linked list where each element in the list is a node and have an integer data. You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

Note: The head represents the first element of the given array.

Examples :

Input: LinkedList: 4->5->6
Output: 457

Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 

Input: linkedlist: 2->4->7->8->9 
Output: 24790


"""


class ListNode:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        
        

def addOne(head):
    #Returns new head of linked List.
    
    def reverse_linkList(head):
        prev = None
        curr = head
        nnext = None
    
        while curr is not None:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext
        
        return prev

        
    temp = reverse_linkList(head)
    
    nnode = temp
    carry, summ, add = 0, 0, 1

    while nnode.next:
        sum = nnode.data + add + carry
        nnode.data = sum % 10
        carry = sum//10
        add = 0
        nnode = nnode.next
        
        if carry==0:
            break
        
    sum = nnode.data + add + carry
    nnode.data = sum % 10
    carry = sum//10
       
    if carry:
        nnode.next = Node(carry)

    return reverse_linkList(temp)



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
    
    res_head = addOne(head)
    
    print("Linked list after reversed:")
    print_linked_list(res_head)
    
  
