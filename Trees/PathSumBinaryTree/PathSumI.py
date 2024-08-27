"""
# 112. Path Sum in Binary Tree

Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.



                   5		
                 /   \      
                2    12		
               / \   / \    
              1   3 9  21	                    
                      / \               
                     19	25	 

"""
from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def levelOrder(root):
    level = []
    lst = []
    
    if not root:
        return root
        
    Q = deque([None, root])
    
    while (True):
        x = Q.pop()
        if x:
            level.append(x.data)
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
  
  
  
def hasPathSum(root, targetSum):
    def dfs(node, currSum):
        if not node:
            return False
        currSum += node.data
        if not node.left and not node.right:
            return currSum == targetSum
        return (dfs(node.left, currSum) or dfs(node.right, currSum))
    return dfs(root, 0)
    
    
        
if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(12)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(9)
    root.right.right = Node(21)
    root.right.right.left = Node(19)
    root.right.right.right = Node(25)
    
    print("Level order traversal of the given binary tree: ", levelOrder(root))
    
    targetSum = 10
    
    res1 = hasPathSum(root, targetSum)
    print("Count Good Nodes in Binary Tree: ", res1)
    
    
    
