'''
# 95. Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]

'''
from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            
            res = []
            for val in range(left, right+1):
                for leftTree in generate(left, val-1):
                    for rightTree in generate(val+1, right):
                        root = TreeNode(val, leftTree, rightTree)
                        res.append(root)
            return res
        return generate(1, n)
        


def print_tree(root):
    """Print tree in level-order, including None children."""
    if root is None:
        print("[]")
        return

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()

        if node is None:
            result.append(None)
            continue

        result.append(node.val)

        queue.append(node.left)
        queue.append(node.right)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    print(result)

# def inorder(root, lst):
#     # Note: Inorder of a BST is always sorted and same for each unique combinations
#     if not root:
#         return None
#     inorder(root.left, lst)
#     lst.append(root.val)
#     inorder(root.right, lst)
    
#     return lst

# def preorder(root, lst):
#     if not root:
#         return None
#     lst.append(root.val)
#     preorder(root.left, lst)
#     preorder(root.right, lst)
    
#     return lst
    
        
if __name__ == "__main__":
    n = 3
    res = Solution().generateTrees(n)
    
    for i, eachTree in enumerate(res, 1):
        print(f"Tree {i}:")
        # print_tree(eachTree)
        # print("Preorder")
        print(preorder(eachTree, []))
