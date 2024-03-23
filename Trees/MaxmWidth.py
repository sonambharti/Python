"""
/*
Given a Binary Tree, find the maximum width of the Binary Tree. 
Maximum width is defined as the maximum number of nodes at any level.



    5			<---->		        5
   / \                             / \
  1   8			<---->            8   1 
   \   \                         /   /
    4   9		<---->          9   4
       /                         \
      2			<---->             2
"""
# Function to return a maximum number of nodes at any level of the binary tree.
from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def getMaxWidth(root):
    level = []
    maxm = 0
    Q = deque([None, root])
    if not root:
        return maxm
    while True:
        x = Q.pop()
        if x:
            level.append(x.data)
            if x.left:
                Q.appendleft(x.left)
            if x.right:
                Q.appendleft(x.right)
        else:
            maxm = max(maxm, len(level))
            level = []
            if Q:
                Q.appendleft(None)
            else:
                break
    return maxm
    
root = Node(5)
root.left = Node(1)
root.right = Node(8)
root.left.right = Node(4)
root.right.right = Node(9)
root.right.right.left = Node(2)

res = getMaxWidth(root)
print("Get Maxm Width of Binary Tree: ", res)
