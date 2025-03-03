'''
# Maximum path sum from any node

Given a binary tree, the task is to find the maximum path sum. The path may start 
and end at any node in the tree.

Examples:

Input: root[] = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
Output: 42

Input: root[] = [-17, 11, 4, 20, -2, 10]
Output: 31

'''

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        


class Solution:
    def solve(self,root,ans):
        if root:
            l=max(0,self.solve(root.left,ans))
            r=max(0,self.solve(root.right,ans))
            ans[0]=max(ans[0],l+r+root.data)
            return root.data+max(l,r)
        return 0
        
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        ans=[-float("inf")]
        self.solve(root,ans)
        return ans[0]



if __name__ == "__main__":
    # root = [10, 2, 10, 20, 1, N, -25, N, N, N, N, 3, 4]
    root = Tree(10)
    root.left = Tree(2)
    root.right = Tree(10)
    root.left.left = Tree(20)
    root.left.right =Tree(1)
    root.right.right = Tree(-25)
    root.right.right.left = Tree(3)
    root.right.right.right = Tree(4)
    
    
    obj = Solution()

    print(obj.findMaxSum(root))
    
    
