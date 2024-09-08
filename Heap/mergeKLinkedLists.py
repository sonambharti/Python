"""
# 23. Merge Sorted List

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

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

    
import heapq

def mergeKLists_usingPriorityQueue(lists):
    # Min-heap to keep track of the smallest element
    min_heap = []
    
    # Push the head of each list into the heap with (unique_index, node.val, node)
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i, l))
    
    # Dummy node to help with merging
    dummy = ListNode()
    current = dummy
    
    # Merge process
    while min_heap:
        # Pop the smallest node from the heap (using the node's value for comparison)
        smallest_val, i, smallest_node = heapq.heappop(min_heap)
        current.next = smallest_node
        current = current.next
        
        # If there is a next node in the list, push it into the heap
        if smallest_node.next:
            heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))
    
    # Return the merged list, which starts from dummy.next
    return dummy.next


if __name__ == "__main__":

    # Sample input of linked lists
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    # print(print_linked_list(list1))
    # print(print_linked_list(list2))
    # print(print_linked_list(list3))
    lists = [list1, list2, list3]

    merged_list = mergeKLists_usingPriorityQueue(lists)

    # Print the merged linked list
    print("Merged Linked List:")
    print_linked_list(merged_list)
    
        
        
  
    
  
