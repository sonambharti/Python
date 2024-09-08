"""
# 725. Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k 
consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a 
size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring 
earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and 
earlier parts are a larger size than the later parts.


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
    print("None", end = " ")
    

def splitListToParts(head, k):
    
    def getListLength(head):
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        # print("size of list = ", n)
        return n
        
    n = getListLength(head)
    partSize = n//k
    extra = n % k
    
    ans = []
    curr = head
    prev = None
    
    while head:
        eachListSize = partSize
        ans.append(curr)
        
        while eachListSize > 0:
            prev = curr
            curr = curr.next
            eachListSize -= 1
            
        if extra != 0 and curr:
            extra -= 1
            prev = curr
            curr = curr.next
        
        if prev:
            head = curr
            prev.next = None
            
    while len(ans) != k:
        ans.append(None)
        
    return ans
    
    




if __name__ == "__main__":
    # Helper function to print the linked list

    # Creating a linked list with a loop
    head = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(8)
    node4 = ListNode(9)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    
    print("Linked list:")
    print_linked_list(head)
    
    k = 6

    res = splitListToParts(head, k)
    
    print("\nSplited Lists are: ", end = "")
    print("[", end = " ")
    for lists in res:
        print_linked_list(lists)
        print(",", end = " ")
    print("]")
        
        
  
    
  
