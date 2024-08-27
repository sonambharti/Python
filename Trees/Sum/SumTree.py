"""
# Sum Tree

Given a Binary Tree. Check for the Sum Tree for every node except the leaf node. 
Return true if it is a Sum Tree otherwise, return false.

A SumTree is a Binary Tree where the value of a node is equal to the sum of the 
nodes present in its left subtree and right subtree. An empty tree is also a Sum 
Tree as the sum of an empty tree can be considered to be 0. A leaf node is also 
considered a Sum Tree.

Examples :

Input:
    3
  /   \    
 1     2
Output: true
Explanation: The sum of left subtree and right subtree is 1 + 2 = 3, which is the 
value of the root node. Therefore,the given binary tree is a sum tree.
"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
def is_sum_tree(node):
    # code here
    def isSumT(node):
        if node is None:
            return True, 0
            
        if not node.left and not node.right:
            return True, node.data
            
        is_left_sum_tree, left_sum = isSumT(node.left)
        is_right_sum_tree, right_sum = isSumT(node.right)
        
        # Current node's value should be equal to the sum of values of left and right subtrees
        is_current_sum_tree = (node.data == left_sum + right_sum)
        
        # Return true if the current node is a sum tree and both left and right subtrees are sum trees
        return is_current_sum_tree and is_left_sum_tree and is_right_sum_tree, node.data + left_sum + right_sum

    
    isSum, _ = isSumT(node)
    return isSum
    
    
if __name__ == "__main__":
    # root = Tree(11)
    # root.left = Tree(4)
    # root.right = Tree(7)
    # root.left.left = Tree(2)
    # root.left.right =Tree(2)
    # root.right.left = Tree(5)
    # root.right.right = Tree(2)
    
    # root.left.left.left = Tree(1)
    # root.left.left.right = Tree(1)
    
    root = Tree(70)
    root.left = Tree(20)
    root.right = Tree(30)
    root.left.left = Tree(10)
    root.left.right =Tree(10)

    
    print("Is given tree a sum tree: ", is_sum_tree(root))
