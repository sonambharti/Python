
"""
/*
 Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:

Input: root = [2,1,3]
Output: 1


Example 2:

Input: root = [5, 1, 8, 4, 9, 2]
Output: 1

    5					
   / \
  1   8			
   \   \
    4   9		
       /
      2			
"""
# Function to return a list containing elements of bottom left view of the binary tree.

from collections import deque, defaultdict

class Node():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        

def bottomLeftView(root):
    if not root:
        return root

    level = []
    lst = []
    Q = deque([None, root])

    while True:
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

    res = lst[-1][0]
    return res
    
    
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(1)
    root.right = Node(8)
    root.left.right = Node(4)
    root.right.right = Node(9)
    root.right.right.left = Node(2)
    
    res = bottomLeftView(root)
    print(res)
