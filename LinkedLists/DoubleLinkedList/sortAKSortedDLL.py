'''
# Sort a k sorted doubly linked list

Given a doubly linked list, each node is at most k-indices away from its target position.
The problem is to sort the given doubly linked list. The distance can be assumed in either
of the directions (left and right).

Examples :

Input: Doubly Linked List : 3 <-> 2 <-> 1 <-> 5 <-> 6 <-> 4 , k = 2
Output: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6

Explanation: After sorting the given 2-sorted list is 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6.
Input: Doubly Linked List : 5 <-> 6 <-> 7 <-> 3 <-> 4 <-> 4 , k = 3
Output: 3 <-> 4 <-> 4 <-> 5 <-> 6 <-> 7

Explanation: After sorting the given 3-sorted list is 3 <-> 4 <-> 4 <-> 5 <-> 6 <-> 7.
Expected Time Complexity: O(n*logk)
Expected Auxiliary Space: O(k)

'''

class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        

def print_doubly_linked_list(head):
    prev = None
    print('None -> ', end = "")
    while(head != None):
        print(head.data, end=" -> ")
        prev=head
        head=head.next
    print('None')
    print('None <- ', end = "")
    while(prev != None):
        print(prev.data, end=" <- ")
        prev=prev.prev
    print('None')
    
    
from heapq import *
def sortAKSortedDLL(head, k):
    # Code Here
    temp1, temp2 = head, head
    min_heap = []
    while temp2:
        heappush(min_heap, temp2.data)
        if len(min_heap)==k+1:
            temp1.data = heappop(min_heap)
            temp1 = temp1.next
        temp2 = temp2.next
    
    while (len(min_heap) != 0):
        temp1.data = heappop(min_heap)
        temp1 = temp1.next
    return head
            
            
            
if __name__ == "__main__":
    head = DoublyLinkedList(3)
    node2 = DoublyLinkedList(2)
    node3 = DoublyLinkedList(1)
    node4 = DoublyLinkedList(5)
    node5 =DoublyLinkedList(6)
    node6 = DoublyLinkedList(4)
    head.prev = None
    head.next = node2
    node2.prev = head
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5
    node6.next = None
    print_doubly_linked_list(head)
    k = 2
    res = sortAKSortedDLL(head, k)
    print("Printing the sorted doubly linked list ")
    print_doubly_linked_list(res)
