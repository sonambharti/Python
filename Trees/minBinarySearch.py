"""
Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

                5		
               / \      
              4   6		
             /     \    
            3       7	                    
           /                    
          1		 

In a Binary search tree, the value of left node must be smaller than the parent node, 
and the value of right node must be greater than the parent node.
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def minValue(root):
        # Your code here
        while root.left:
            root = root.left
        
        return root.data
    
root = Node(5)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(3)
root.right.right = Node(7)
root.left.left.left = Node(1)

res1 = minValue(root)
print("Minm Value of given Binary Search Tree: ", res1)
