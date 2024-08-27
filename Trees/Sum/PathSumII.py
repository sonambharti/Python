"""
# 113. Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths 
where the sum of the node values in the path equals targetSum. Each path should be 
returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf
is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 



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
  
  
  
def PathSum(root, targetSum):
    res = []
    path = []
    def dfs(node, path, curr_sum):
        curr_sum += node.data
        temp = path + [node.data]

        if node.left:
            dfs(node.left, temp, curr_sum)
        if node.right:
            dfs(node.right, temp, curr_sum)
        if not node.left and not node.right and curr_sum == targetSum:
            res.append(temp)
    
    if not root:
        return []
    dfs(root, path, 0)
    return res
    
        
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
    
    res1 = PathSum(root, targetSum)
    print("Path of the target Sum root-to-leaf: ", res1)
    
    
    
