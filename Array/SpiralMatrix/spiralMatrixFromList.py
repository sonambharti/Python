'''
# 2326. Spiral Matrix IV

You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), 
starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

'''



"""
        l   r
    t [ 1 2 3 ],
        [ 4 5 6 ],        
    b [ 7 8 9 ]

    direction -> d
    # 1 2 3     -> row d = 0
    # 6 9       -> col d = 1
    # 8 7       -> row d = 2
    # 4         -> col d = 3
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
    
def getListLength(head):
    lenl = 0
    temp = head
    while temp:
        lenl += 1
        temp = temp.next
    # print("size of list = ", n)
    return lenl

def spiralMatrix(m, n, head):
    
    res_mat = [[-1] * n for _ in range(m)]

    lenl = getListLength(head)

    l = 0
    r = n
    t = 0
    b = m

    while l < r and t < b:
        for i in range(l, r):
            if head:
                res_mat[t][i] = head.val
                head = head.next
        t += 1

        for i in range(t, b):
            if head:
                res_mat[i][r-1] = head.val
                head = head.next
        r -= 1

        if not (l < r and t < b):
            break

        for i in range(r-1, l-1, -1):
            if head:
                res_mat[b-1][i] = head.val
                head = head.next
        b -= 1

        for i in range(b-1, t-1, -1):
            if head:
                res_mat[i][l] = head.val
                head = head.next
        l += 1
    
    return res_mat
    
if __name__ == "__main__":
    m = 3
    n = 5
    head = create_linked_list([3,0,2,6,8,1,7,9,4,2,5,5,0])
    print_linked_list(head)
    res = spiralMatrix(m, n, head)
    print("Print the resultant matrix: ", res)
