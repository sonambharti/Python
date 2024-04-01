"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in 
the sequence has an edge connecting them. A node can only appear in the sequence at 
most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


                   5		
                 /   \      
                2    12		
               / \   / \    
              1   3 9  21	                    
                      / \               
                     19	25	 

Input: root = [1,2,3]
Output: 6
"""

class Node():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def maxPathSum(root):
        
    maxm = -10**9
    
    def maxSum(root):
        nonlocal maxm
        if not root:
            return 0
        left_sum = max(maxSum(root.left), 0)
        right_sum = max(maxSum(root.right), 0)
        
        # Update the maximum path sum found so far
        current_sum = root.val + left_sum + right_sum
        maxm = max(maxm, current_sum)
        
        # Return the maximum sum achievable by considering the current node
        return root.val + max(left_sum, right_sum)
    
    maxSum(root)
    return maxm
    
root = Node(5)
root.left = Node(2)
root.right = Node(12)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

res1 = maxPathSum(root)
print("Maxm Sum Path: ", res1)
