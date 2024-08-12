"""
# 1038. Binary Search Tree to Greater Sum Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that 
every key of the original BST is changed to the original key plus the sum of all keys 
greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

class Tree:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
    
def inorder(root, lst):
    if root:
        inorder(root.left, lst)
        lst.append(root.val)
        inorder(root.right, lst)
    return lst
    
def preorder(root, lst):
    if root:
        lst.append(root.val)
        preorder(root.left, lst)
        preorder(root.right, lst)
    return lst
    
    
    
from collections import deque

def levelOrder(root):
    level = []
    lst = []
    
    if not root:
        return root
        
    Q = deque([None, root])
    
    while (True):
        x = Q.pop()
        if x:
            level.append(x.val)
            if x.left:
                Q.appendleft(x.left)
            if x.right:
                Q.appendleft(x.right)
        
        else:
            lst.append(level)
            level = []
            
            if Q:
                Q.appendleft(None)
            else:
                break
    return lst
    
    
def bstToGst(root):
    sume = 0
    def dfs(root):
        nonlocal sume
        if not root:
            return
        dfs(root.right)
        root.val += sume
        sume = root.val
        dfs(root.left)
    
    dfs(root)
    return root
    
    
    
if __name__ == "__main__":
    
    root = Tree(4)
    root.left = Tree(1)
    root.right = Tree(6)
    root.left.left = Tree(0)
    root.left.right =Tree(2)
    root.left.right.right =Tree(3)
    root.right.left = Tree(5)
    root.right.right =Tree(7)
    root.right.right.right =Tree(8)
    
   
    lst = []
    # preorder(root, lst)
    lst = levelOrder(root)
    print("Binary Search Tree: \n", lst)
    
    lst1 = []
    bstToGst(root)
    # preorder(root, lst1)
    lst1 = levelOrder(root)
    print("Greater Sum Tree: \n", lst1)
