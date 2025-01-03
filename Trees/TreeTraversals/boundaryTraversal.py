'''
# Tree Boundary Traversal

Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left Boundary: This includes all the nodes on the path from the root to the leftmost leaf node. You must 
prefer the left child over the right child when traversing. Do not include leaf nodes in this section.

Leaf Nodes: All leaf nodes, in left-to-right order, that are not part of the left or right boundary.

Reverse Right Boundary: This includes all the nodes on the path from the rightmost leaf node to the root, 
traversed in reverse order. You must prefer the right child over the left child when traversing. Do not 
include the root in this section if it was already included in the left boundary.

Note: If the root doesn't have a left subtree or right subtree, then the root itself is the left or right boundary. 

Examples:

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N] 
        1 
      /   \
     2     3  
    / \   / \ 
   4   5 6   7
      / \
     8   9
   
Output: [1, 2, 4, 8, 9, 6, 7, 3]
Explanation:

Input: root[] = [1, 2, N, 4, 9, 6, 5, N, 3, N, N, N, N 7, 8] 
            1
           /
          2
        /  \
       4    9
     /  \    \
    6    5    3
             /  \
            7     8

Output: [1, 2, 4, 6, 5, 7, 8]
'''

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        

def solveLeft(root, ans):
    if not root or not root.left and not root.right:
        return
    ans.append(root.data)
    if root.left:
        solveLeft(root.left, ans)
    else:
        solveLeft(root.right, ans)


def solveLeaf(root, ans):
    if not root:
        return
    if not root.left and not root.right:
        ans.append(root.data)
        return
    solveLeaf(root.left, ans)
    solveLeaf(root.right, ans)


def solveRight(root, ans):
    if not root or not root.left and not root.right:
        return
    
    if root.right:
        solveRight(root.right, ans)
    else:
        solveRight(root.left, ans)
        
    ans.append(root.data)
    
    
def boundaryTraversal(root):
    # Code here
    ans = []
    if not root:
        return ans
    ans.append(root.data)
    if not root.left and not root.right:
        return ans
    solveLeft(root.left, ans)
    solveLeaf(root, ans)
    solveRight(root.right, ans)
    
    return ans
    
    
if __name__ == "__main__":
    root = Tree(90)
    root.left = Tree(80)
    root.right = Tree(75)
    root.left.left = Tree(70)
    root.left.left.left = Tree(7)
    root.left.right =Tree(79)
    root.right.left = Tree(69)
    root.right.right = Tree(65)
    
    print("Boundary Traversal of the tree: ",boundaryTraversal(root))
    
