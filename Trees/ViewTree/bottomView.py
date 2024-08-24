"""
/*
Given a binary tree, return an array where elements represent the bottom view of the 
binary tree from left to right.

Note: If there are multiple bottom-most nodes for a horizontal distance from the root, 
then the latter one in the level traversal is considered. For example, in the below 
diagram, 3 and 4 are both the bottommost nodes at a horizontal distance of 0, here 4 
will be considered.




    5					
   / \
  1   8			
   \   \
    4   9		
       /
      2			
"""
# Function to return a list containing elements of bottom view of the binary tree.

from collections import deque, defaultdict

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def bottomView(root):
    res = []
    if root is None:
        return res
    
    Q = deque()
    Q.appendleft((root, 0))
    map_level = defaultdict(int)
    
    while Q:
        node, line = Q.pop()
        map_level[line] = node.data
        
        if node.left:
            Q.appendleft((node.left, line - 1))
        if node.right:
            Q.appendleft((node.right, line + 1))
            
    for key, value in sorted(map_level.items()):
        res.append(value)
        
    return res


root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(2)

res = bottomView(root)
print(res)
