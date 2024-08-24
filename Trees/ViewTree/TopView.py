"""
#  Top View of Binary Tree

Given below is a binary tree. The task is to print the top view of binary tree. 
Top view of a binary tree is the set of nodes visible when the tree is viewed 
from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6       7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are 
outside the shadow of the tree and are at same position then consider the left 
ones only(i.e. leftmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. 
Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3

Example 2:

    5				
   / \
  1   8		
   \   \
    4   9		
       /
      2			
"""
# Function to return a list containing elements of Top view of the binary tree.

from collections import deque, defaultdict

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def TopView(root):
    res = []
    if root is None:
        return res
    
    Q = deque()
    Q.appendleft([root, 0])
    map_level = {}
    
    while Q:
        node, line = Q.pop()
        
        if line not in map_level:
                map_level[line] = node.data
                
        if node.left:
            Q.appendleft([node.left, line - 1])
        if node.right:
            Q.appendleft([node.right, line + 1])
    
            
    for key, value in sorted(map_level.items()):
        res.append(value)
        
    return res

root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(2)

res = TopView(root)
print(res)
