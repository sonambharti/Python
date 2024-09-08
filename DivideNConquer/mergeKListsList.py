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


# Solution class with the divide and conquer approach
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)
    
    def mergeKListsHelper(self, lists, left, right):
        # Base case: If there's only one list, return it
        if left == right:
            return lists[left]
        
        # Divide step: Find the middle of the lists
        mid = (left + right) // 2
        
        # Conquer step: Recursively merge the left and right halves
        left_merged = self.mergeKListsHelper(lists, left, mid)
        right_merged = self.mergeKListsHelper(lists, mid + 1, right)
        
        # Merge the two halves
        return self.mergeTwoLists(left_merged, right_merged)
    
    def mergeTwoLists(self, l1, l2):
        # Helper function to merge two sorted linked lists
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach the remaining nodes
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next


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


# Print Linked List
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")



if __name__ == "__main__":

    # Sample input of linked lists
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    lists = [list1, list2, list3]

    # Create Solution object and call mergeKLists
    solution = Solution()
    merged_list = solution.mergeKLists(lists)
    

    # Print the merged linked list
    print("Merged Linked List:")
    print_linked_list(merged_list)
    
        
        
# Complexity: O(n*log k), where k = no. of total list,
# n = no of elements in each link list in the list
    
  
