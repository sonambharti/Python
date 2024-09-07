"""
/*
Given the root of a binary tree, imagine yourself standing in front of the mirror.
Return the values of the inorder traversal of the nodes.


    5			                          5
   / \                             / \
  1   8			                      8   1 
   \   \    <--------------->    /   /
    4   9		                    9   4
       /                         \
      2			                      2
"""
# Function to return a list containing elements of mirror image of the binary tree.
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
    
def recursive_mirror_tree(root):
    # Code here
    if root is None:
        return None
    lst = []
    # Swap left and right subtrees
    root.left, root.right = root.right, root.left
    
    # Recursively mirror left and right subtrees
    recursive_mirror_tree(root.left)
    recursive_mirror_tree(root.right)
    lst = inorder(root, lst)
    return lst
    
def mirror_tree_stack(root):
    # Code here
    stack = [root]
    lst = []
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    
    lst = inorder(root, lst)
    return lst
    
root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(2)
lst1 = []
print("Inorder Traversal of Original tree: ", inorder(root, lst1))
# res = recursive_mirror_tree(root)
# print("Recursive approach Mirror Tree: ", res)

res1 = mirror_tree_stack(root)
print("Mirror Trees using Stack: ", res1)
