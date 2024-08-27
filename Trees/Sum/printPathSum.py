"""
# Paths from root with a specified sum

Given a Binary tree and a sum S, print all the paths, starting from root, that sums upto 
the given sum. Path not necessarily end on a leaf node.

Example 1:

Input : 
sum = 8
Input tree
         1
       /   \
     20      3
           /    \
         4       15   
        /  \     /  \
       6    7   8    9      

Output :
1 3 4
Explanation : 
Sum of path 1, 3, 4 = 8.
Example 2:

Input : 
sum = 38
Input tree
          10
       /     \
     28       13
           /     \
         14       15
        /   \     /  \
       21   22   23   24
Output :
10 28
10 13 15  
Explanation :
Sum of path 10, 28 = 38 and
Sum of path 10, 13, 15 = 38.
Your task :
You don't have to read input or print anything. Your task is to complete the function 
printPaths() that takes the root of the tree and sum as input and returns a vector of
vectors containing the paths that lead to the sum.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(N2)

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
        if curr_sum == targetSum:
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
    
    targetSum = 17
    
    res1 = PathSum(root, targetSum)
    print("Path of the target Sum from root to a node: ", res1)
    
    
    
