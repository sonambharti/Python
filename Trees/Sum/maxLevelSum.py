"""
# 1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2



    5			<-- 5		        <= Level 1
   / \
  1   8			<-- 8 + 1 = 9       <= Level 2
   \   \
    4   9		<-- 9 + 4 = 13      <= Level 3
       /
      2			<-- 2               <= Level 4

"""

from collections import deque

class Node():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def maxLevelSum(root):
    if not root:
        return []
    
    
    Level = 1
    minLevel = 1
    maxSum = - float('infinity')
    levelSum = 0
    Q = deque([None, root])
    
    while Q:
        x = Q.pop()
        if x:
            levelSum += x.val
            if x.left:
                Q.appendleft(x.left)
            if x.right:
                Q.appendleft(x.right)
                
        else:
            if levelSum > maxSum:
                maxSum = levelSum
                minLevel = Level
            levelSum = 0
            Level += 1
            
            if Q:
                Q.appendleft(None)

            
    return minLevel


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(1)
    root.right = Node(8)
    root.left.right = Node(4)
    root.right.right = Node(9)
    root.right.right.left = Node(2)
    
    res = maxLevelSum(root)
    print("Maximum sum is at level: ",res)
