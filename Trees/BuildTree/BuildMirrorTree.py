'''
# Mirror Tree

Given a binary tree, convert the binary tree to its Mirror tree.

Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of
all non-leaf nodes interchanged.     

Examples:

Input: root[] = [1, 2, 3, N, N, 4]
Output: [1, 3, 2, N, 4]
Explanation: 

'''

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    
        
        
class Solution:
    def mirror(self, root):
        # Code here
        # Code here
        if root is None:
            return None
        # lst = []
        # Swap left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively mirror left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
        # return root
    

if __name__ == "__main__":
    # root = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4] # level order traversal 
    root = Tree(10)
    root.left = Tree(2)
    root.right = Tree(10)
    root.left.left = Tree(20)
    root.left.right =Tree(1)
    root.right.right = Tree(-25)
    root.right.right.left = Tree(3)
    root.right.right.right = Tree(4)
    
    
    obj = Solution()
    
    print("Inorder Traversal before mirroring:\n")
    inorder(root)
    print()
    
    obj.mirror(root)
    print("Inorder Traversal after mirroring:\n")
    inorder(root)
    # print()
    
    
