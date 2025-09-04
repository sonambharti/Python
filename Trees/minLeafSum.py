"""
Given a binary tree containing n nodes. The problem is to get the sum of all the leaf nodes which are at 
minimum level in the binary tree.

Input : 
              1
            /  
           2     3
         /  \   /  \
        4   5   6   7
           /     \
          8       9

Output : 11
Leaf nodes 4 and 7 are at minimum level.
Their sum = (4 + 7) = 11.
"""
from collections import deque

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def minLeafSum(root):
    if not root.left and not root.right:
        return root.val

    res = 0
    q = deque([None, root])

    while q:
        el = q.pop()
        if el:
            if not el.left and not el.right:
                res += el.val
            if el.left:
                q.appendleft(el.left)
            if el.right:
                q.appendleft(el.right)
        else:
            if q:
                q.appendleft(None)
            if res:
                return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.left = Node(6)
root.right.left.right = Node(9)
root.right.right = Node(7)

print(getSum(root))
