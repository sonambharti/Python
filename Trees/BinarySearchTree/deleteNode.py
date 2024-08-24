"""
# 450. Delete node in a Binary Search Tree

Given a root node reference of a BST and a key, delete the node with the given key in 
the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
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
  
  
  
# Delete Node and replace the parent with right subtree  
def deleteNodeRightBST(root, X):
    # code here.
    
    def helper(root):
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            
        leftChild = root.left
        lastLeft = findLastChild(root.right)
        lastLeft.left = leftChild
        return root.right
        
    def findLastChild(root):
        if not root.left:
            return root
        return findLastChild(root.left)
        
        
    if not root:
        return None
    
    if root.data == X:
        return helper(root)
        
    temp = root
    
    while root:
        if root.data > X:
            if root.left and root.left.data == X:
                root.left = helper(root.left)
                break
            else:
                root = root.left
        else:
            if root.right and root.right.data == X:
                root.right = helper(root.right)
                break
            else:
                root = root.right
    return temp
        

    
    
# Delete Node and replace the parent with left subtree
def deleteNodeLeftBST(root, val):
    def helper(root):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
            
        rightChild = root.right
        lastRight = findLastChild(root.left)
        lastRight.right = rightChild
        return root.left
        
    def findLastChild(root):
        if not root.right:
            return root
        return findLastChild(root.right)
        
    if not root:
        return None
    
    if root.data == val:
        return helper(root)
    
    temp = root
    
    while root:    
        if root.data > val:
            if root.left and root.left.data == val:
                root.left = helper(root.left)
                break
            else:
                root = root.left
                
        else:
            if root.right and root.right.data == val:
                root.right = helper(root.right)
                break
            else:
                root = root.right
    return temp 
        
    
        
    
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
    
    
    
    res1 = deleteNodeLeftBST(root, 12)
    print("Level Order after deleting the given node: ", levelOrder(res1))
    
    
    res2 = deleteNodeRightBST(root, 12)
    print("Level Order after deleting the given node: ", levelOrder(res2))
    
    
