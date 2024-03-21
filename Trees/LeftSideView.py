"""
/*
Given the root of a binary tree, imagine yourself standing on the left side of it.
Return the values of the nodes you can see ordered from top to bottom.


    5			<-- 5		
   / \
  1   8			<-- 1
   \   \
    4   9		<-- 4
       /
      2			<-- 2
"""
# Function to return a list containing elements of left view of the binary tree.
from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def LeftView(root):
    if not root:
        return []
    level = []
    res = []
    Q = deque([None, root])
    
    while Q:
        x = Q.pop()
        if x:
            level.append(x.data)
            if x.left:
                Q.appendleft(x.left)
            if x.right:
                Q.appendleft(x.right)
                
        else:
            #lst.append(level)
            if len(level)!=0:
                res.append(level[0])
            level = []
            
            if Q:
                Q.appendleft(None)
    return res
    
def optimized_LeftView(root):
    # code here
    if not root:
        return []
    level = []
    res = []
    Q = deque([root])
    
    while Q:
        level_size = len(Q)
        
        for i in range(level_size):
            node = Q.popleft()
            if i == 0:  # Only consider the first node at each level
                res.append(node.data)
            
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
    
    return res
    
root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(2)

res = LeftView(root)
print(res)

res1 = optimized_LeftView(root)
print(res)
