"""
# 1019. Next Greater Node in Linked List
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, 
find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the 
ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

Example 1:


Input: head = [2,1,5]
Output: [5,5,0]
Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]


"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def create_link_list(arr):
    n = len(arr)
    head = ListNode(arr[0])
    dummy_head = head
    
    for i in range(1, n):
        dummy_head.next = ListNode(arr[i])
        dummy_head = dummy_head.next
    return head
    
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
        
class Solution:
    def nextLargerNodes_Brute(self, head):
        if not head:
            return []
        
        dummy_node = head
        tail = head
        n = 1
        val_list = []
        val_list.append(tail.val)
        while tail.next:
            tail = tail.next
            val_list.append(tail.val)
            n += 1

        res = [0] * n
        
        for i in range(n):
            maxm = val_list[i]
            for j in range(i+1, n):
                maxm = max(maxm, val_list[j])
                if maxm > val_list[i]:
                    res[i] = maxm
                    break
        return res
        
    
    def nextLargerNodes(self, head):
        n = 0
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
            n += 1

        res = [0] * n
        st = []
        
        for i in range(n):
            while st and val_list[i] > val_list[st[-1]]:
                indx = st.pop()
                res[indx] = val_list[i]
            st.append(i)
        return res
        
    

if __name__ == "__main__":
    # Helper function to print the linked list
    arr = [1,7,5,1,9,2,5,1]
    
    head = create_link_list(arr)
    
    print("Linked list:")
    print_linked_list(head)
    
    largerNodeList = Solution().nextLargerNodes(head)
    print(largerNodeList)
    
    
  
