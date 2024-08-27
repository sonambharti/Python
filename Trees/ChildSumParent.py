"""
# Children Sum in a Binary Tree

Given a binary tree having n nodes. Check whether all of its nodes have the value equal to the sum of their child nodes. 
Return 1 if all the nodes in the tree satisfy the given properties, else it return 0.

For every node, data value must be equal to the sum of data values in left and right children. Consider data value as 0 
for NULL child.  Also, leaves are considered to follow the property.

Example 1:

Input:
Binary tree
       35
      /   \
     20  15
    /  \  /  \
   15 5 10 5
Output: 
1
Explanation: 
Here, every node is sum of its left and right child.
Example 2:

Input:
Binary tree
       1
     /   \
    4    3
   /  
  5    
Output: 
0
Explanation: 
Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node.
Hence, this tree does not satisfy the given condition.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isSumProperty() that takes 
the root Node of the binary tree as input and returns 1 if all the nodes in the tree satisfy the following 
properties, else it returns 0.

Expected Time Complexiy: O(n).
Expected Auxiliary Space: O(Height of the Tree).
"""
from collections import deque

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def childSumParent(root):
    if not root or not root.left and not root.right:
        return 1
        
    if root.left != None:
        l = root.left.data
    if root.right != None:
        r = root.right.data
    
    if root.data == l+r and childSumParent(root.left)==1 and childSumParent(root.right)==1:
        return 1
    
    return 0
    
    
root = Tree(90)
root.left = Tree(45)
root.right = Tree(45)
root.left.left = Tree(30)
root.left.right =Tree(15)
root.right.left = Tree(25)
root.right.right = Tree(20)


print("Given tree is child sum Parent: ", childSumParent(root))


   
root1 = Tree(90)
root1.left = Tree(45)
root1.right = Tree(55)
root1.left.left = Tree(30)
root1.left.right =Tree(15)
root1.right.left = Tree(25)
root1.right.right = Tree(20)


print("Given tree is child sum Parent: ", childSumParent(root1))


