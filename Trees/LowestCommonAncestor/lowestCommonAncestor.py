"""
# 236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1



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
    
    
  
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root

    leftSubT = lowestCommonAncestor(root.left, p, q)
    rightSunT = lowestCommonAncestor(root.right, p, q)

    if not leftSubT:
        return rightSunT
    elif not rightSunT:
        return leftSubT
    else: # both left and right subtree are there so we found the result
        return root
        
        
        
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
    
    # p = 12
    p = root.right
    # q = 1
    # q = root.left.left
    q = root.right.left # q = 9
    
    res1 = lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor between given nodes is: ", res1.data)
    
    print("Print the whole subtree of th common ancesstor node: ", levelOrder(res1))
    
   