'''
# Construct Tree from Inorder and Preorder

Given two arrays representing the inorder and preorder traversals of a binary tree, 
construct the tree and return the root node of the constructed tree.

Note: The output is written in postorder traversal.

Examples:

Input: inorder[] = [1, 6, 8, 7], preorder[] = [1, 6, 7, 8]
Output: [8, 7, 6, 1]

Input: inorder[] = [3, 1, 4, 0, 2, 5], preorder[] = [0, 1, 3, 4, 2, 5]
Output: [3, 4, 1, 5, 2, 0]
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        

from collections import deque 
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
    
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        def helper(preorder, prestart, prend, inorder, instart, inend, hashdict):
            if prestart > prend or instart > inend:
                return None
            root = Node(preorder[prestart])
            inroot = hashdict.get(root.data)
            numsLeft = inroot - instart
            
            root.left = helper(preorder, prestart + 1, prend + numsLeft, inorder, instart, inroot - 1, hashdict)
            root.right = helper(preorder, prestart + numsLeft + 1, prend, inorder, inroot + 1, inend, hashdict)
            
            return root
            
            
        hashdict = {}
        for i in range(len(inorder)):
            hashdict[inorder[i]] = i
        
        root = helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, hashdict)
        return root
        
        
if __name__ == "__main__":
    # inorder = [1, 6, 8, 7]
    # preorder = [1, 6, 7, 8]
    
    inorder = [3, 1, 4, 0, 2, 5]
    preorder = [0, 1, 3, 4, 2, 5]
    
    BuildTree_obj = Solution()
    root = BuildTree_obj.buildTree(inorder, preorder)
    
    print("Level Order Traversal of the tree: ", levelOrder(root))
    
    
    
