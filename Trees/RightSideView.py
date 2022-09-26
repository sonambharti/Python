"""
/*
Given the root of a binary tree, imagine yourself standing on the right side of it.
Return the values of the nodes you can see ordered from top to bottom.


    5			<-- 5		
   / \
  1   8			<-- 8
   \   \
    4   9		<-- 9
       /
      2			<-- 2

*/
"""
from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def solve(root):
    level = []
    #lst = []
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
            res.append(level[-1])
            level = []
            
            if Q:
                Q.appendleft(None)
            #else:
                #break
            
    return res
    
    
    

root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(2)

res = solve(root)
print(res)
