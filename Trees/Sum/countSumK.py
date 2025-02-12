'''
# K sum paths

Given a binary tree and an integer k, determine the number of downward-only paths where the sum 
of the node values in the path equals k. A path can start and end at any node within the tree 
but must always move downward (from parent to child).

Examples:

Input: 
    k = 7
    Inorder: [3, 3, -2, 4, 2, 1, 8, 5, 2]
Output: 3

'''

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

class Solution:
    def __init__(self):
        self.count = 0
    def sumK(self,root,k):
        # code here
        def helper(root, k, path):
            if not root:
                return
            path.append(root.data)
            summ = 0
            
            for i in range(len(path)-1, -1, -1):
                summ += path[i]
                if summ == k:
                    self.count += 1
            helper(root.left, k, path)
            helper(root.right, k, path)
            # Remove the last element (Backtracking step)
            path.pop()

            
        path = []
        helper(root, k, path)
        return self.count
        

if __name__ == "__main__":
    k = 7
    root = Tree(8)
    root.left = Tree(4)
    root.right = Tree(5)
    root.left.left = Tree(3)
    root.left.left.left = Tree(3)
    root.left.left.right =Tree(-2)
    root.left.right =Tree(2)
    root.left.right.left =Tree(1)
    root.right.right = Tree(2)
    
    # print("Inorder Traversal")
    # inorder(root)
    
    obj = Solution()
    print(obj.sumK(root, k))
