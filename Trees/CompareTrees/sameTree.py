"""
# Same Tree / Identical Trees

Given two binary trees, the task is to find if both of them are identical or not.
Note: You need to return true or false, the printing is done by the driver code.

Example 1:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: 
Yes
Explanation: 
There are two trees both having 3 nodes and 2 edges, both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.
Example 2:

Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: 
No
Explanation: There are two trees both having 3 nodes and 2 edges, but both trees are not identical.
Your task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function isIdentical() that takes two roots as parameters and returns true or false. The printing is done by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).
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
    



if __name__ == "__main__":
    #create tree
    
    root1 = Tree(90)
    root1.left = Tree(80)
    root1.right = Tree(75)
    root1.left.left = Tree(70)
    root1.left.right =Tree(79)
    root1.right.left = Tree(69)
    root1.right.right = Tree(65)
    
    root2 = Tree(90)
    root2.left = Tree(80)
    root2.right = Tree(75)
    root2.left.left = Tree(70)
    root2.left.right =Tree(79)
    root2.right.left = Tree(69)
    root2.right.right = Tree(65)
    
    print("Are these trees same: ", sameTree(root1, root2))
    
    

