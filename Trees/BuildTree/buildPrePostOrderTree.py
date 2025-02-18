'''
# Construct Tree from Postorder and Preorder

Given two integer arrays, preorder and postorder where preorder is the preorder traversal
of a binary tree of distinct values and postorder is the postorder traversal of the same 
tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:

Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Note: We can not construct unique binary tree from a given Pre and post order of the Binary Tree.
But, we can create unique full Binary tree from a given Pre and post order of the Binary Tree.
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
        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            val = preorder[pre_start]
            root = Node(val)

            if pre_start == pre_end: # Leaf node 
                return root 

            # Find index of left child in post order 
            idx = pos_map[preorder[pre_start+1]]
            # Calculate size of the left subtree 
            size_left_subtree=idx-post_start+1

            # Recursively build subtrees 
            root.left=helper(pre_start+1,pre_start+size_left_subtree,post_start ,idx)
            root.right=helper(pre_start+size_left_subtree+1,pre_end ,idx+1,post_end-1)

            return root 
        
        pos_map={val:i for i,val in enumerate(postorder)} 
        return helper(0,len(preorder)-1,0,len(postorder)-1)
        
        
if __name__ == "__main__":
    
    # inorder = [3, 1, 4, 0, 2, 5]
    preorder = [0, 1, 3, 4, 2, 5]
    postorder = [3, 4, 1, 5, 2, 0]
    
    BuildTree_obj = Solution()
    root = BuildTree_obj.buildTree(postorder, preorder)
    
    print("Level Order Traversal of the tree: ", levelOrder(root)) # [[0], [1, 2], [3, 4, 5]]
    
    
    
