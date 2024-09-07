"""
# 572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of 
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this 
node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 
"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    if (root1 and not root2) or (not root1 and root2):
        return False
    if root1.data == root2.data:
        return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
    return False
    


def isSubtree(root, subRoot) -> bool:
        
    if not subRoot:
        return True

    if not root:
        return False

    if sameTree(root, subRoot):
        return True
    
    return (
        isSubtree(root.left, subRoot) or 
        isSubtree(root.right, subRoot)
    )
    
    
if __name__ == "__main__":
    #create tree
    root1 = Tree(112)
    root1.left = Tree(90)
    root1.left.left = Tree(80)
    root1.left.right = Tree(75)
    root1.left.left.left = Tree(70)
    root1.left.left.right =Tree(79)
    root1.left.right.left = Tree(69)
    root1.left.right.right = Tree(65)
    
    root1.right = Tree(45)
    root1.right.left = Tree(46)
    root1.right.right = Tree(48)
    
    root2 = Tree(90)
    root2.left = Tree(80)
    root2.right = Tree(75)
    root2.left.left = Tree(70)
    root2.left.right =Tree(79)
    root2.right.left = Tree(69)
    root2.right.right = Tree(65)
    
    print("Are these trees same: ", isSubtree(root1, root2))
    
    

