"""
# Merge Given two BSTs, 

Given two BSTs, return elements of merged BSTs in sorted form.

Examples :

Input:
BST1:
       5
     /   \
    3     6
   / \
  2   4  
BST2:
        2
      /   \
     1     3
            \
             7
            /
           6
Output: 1 2 2 3 3 4 5 6 6 7
Explanation: After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.
Input:
BST1:
       12
     /   
    9
   / \    
  6   11
BST2:
      8
    /  \
   5    10
  /
 2
Output: 2 5 6 8 9 10 11 12
Explanation: After merging and sorting the two BST we get 2 5 6 8 9 10 11 12.
Expected Time Complexity: O((m+n)*log(m+n))
Expected Auxiliary Space: O(Height of BST1 + Height of BST2 + m + n)

                   5		
                 /   \      
                2    12		
               / \   / \    
              1   3 9  21	                    
                      / \               
                     19	25	 

"""
from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(root, lst):
    if root:
            
        inorder(root.left, lst)
        lst.append(root.data)
        inorder(root.right, lst)
    return lst

def mergeSortArrays(nums1, nums2, m, n):
    Lptr, Rptr = 0, 0

    arr =[]
    while Lptr < m and Rptr < n :
        if (nums1[Lptr] < nums2[Rptr]):
            arr.append(nums1[Lptr])
            Lptr += 1 
        else:
            arr.append(nums2[Rptr])
            Rptr += 1 

    while Lptr < m :
        arr.append(nums1[Lptr])
        Lptr += 1 
    
    while Rptr < n :
        arr.append(nums2[Rptr])
        Rptr += 1 
    
    return arr

if __name__ == "__main__":
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(6)
    root1.left.left = Node(2)
    root1.left.right = Node(4)
    
    root2 = Node(2)
    root2.left = Node(1)
    root2.right = Node(3)
    root2.right.right = Node(7)
    root2.right.right.left = Node(6)
    
    arr1 = inorder(root1, [])
    arr2 = inorder(root2, [])
    print("InOrder Traversal of 1st tree: ", arr1)
    print("InOrder Traversal of 2nd tree: ", arr2)
    
    m = len(arr1)
    n = len(arr2)
    print("Merged BST inorder: ", mergeSortArrays(arr1, arr2, m, n))
    
    
