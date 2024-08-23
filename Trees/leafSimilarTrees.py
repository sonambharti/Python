"""
# 872. Leaf Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those leaves 
form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
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
        self.val = data
        self.left = None
        self.right = None

def leafSimilar(root1, root2):
    def dfs(node, arr):
        if node is None:
            return
        if not node.left and not node.right:
            arr.append(node.val)
        else:
            dfs(node.left, arr)
            dfs(node.right, arr)
    arr1 = []
    arr2 = []
    dfs(root1, arr1)
    dfs(root2, arr2)
    return arr1 == arr2   
    
    
if __name__ == "__main__":
    root1 = Node(5)
    root1.left = Node(2)
    root1.right = Node(12)
    root1.left.left = Node(1)
    root1.left.right = Node(3)
    root1.right.left = Node(9)
    root1.right.right = Node(21)
    root1.right.right.left = Node(19)
    root1.right.right.right = Node(25)
    
    root2 = Node(19)
    root2.left = Node(1)
    root2.right = Node(12)
    root2.right.left = Node(11)
    root2.right.left.left = Node(3)
    root2.right.left.right = Node(9)
    root2.right.right = Node(21)
    root2.right.right.left = Node(19)
    root2.right.right.right = Node(25)
    
    
    
    res1 = leafSimilar(root1, root2)
    print("Similar leaf trees: ", res1)
