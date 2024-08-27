"""
# 437. Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths 
where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards 
(i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


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
    totalCount = 0
    def helper(node, curr_sum):
        nonlocal totalCount
        if not node:
            return
        helper(node.left, curr_sum + node.data)
        helper(node.right, curr_sum + node.data)
        if curr_sum + node.data == targetSum:
            totalCount += 1

    def dfs(node):
        if not node:
            return
        helper(node, 0)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return totalCount



from collections import defaultdict
def pathSumOptimized(root, targetSum):
    totalCount = 0
    lookup = defaultdict(int)
    lookup[targetSum] = 1

    def dfs(node, curr_sum):
        nonlocal totalCount
        if not node:
            return
        # helper(node, 0)
        curr_sum += node.data
        totalCount += lookup[curr_sum]
        lookup[curr_sum + targetSum] += 1
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        lookup[curr_sum + targetSum] -= 1

    
    dfs(root, 0)
    return totalCount
        
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
    print("Count of the path of target Sum from node to node: ", res1)
    
    res2 = pathSumOptimized(root, targetSum)
    print("Count of the path of target Sum from node to node: ", res2)
    
    
