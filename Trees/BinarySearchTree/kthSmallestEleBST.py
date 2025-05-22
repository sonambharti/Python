'''
#   230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest 
value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''

from typing import Optional

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, inor):
        if root:
            self.inorder(root.left, inor)
            inor.append(root.data)
            self.inorder(root.right, inor)
            
    def kthSmallest(self, root: Optional[Tree], k: int) -> int:
        inor = []
        self.inorder(root, inor)
        # print(inor)
        return inor[k-1]
        
if __name__ == "__main__":
    root = Tree(90)
    root.left = Tree(80)
    root.right = Tree(95)
    root.left.left = Tree(70)
    root.left.right =Tree(89)
    root.right.left = Tree(92)
    root.right.right = Tree(96)
    
    k = 1
    obj = Solution()
    res = obj.kthSmallest(root, k)
    print(f"The {k}th smallest element in this tree is: {res}")
        
        
