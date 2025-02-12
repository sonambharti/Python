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
        

class Solution:
    def __init__(self):
        self.count = 0
        
    def sumK_Bruteforce(self,root,k):
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
        
        
    # Using Prefix sum + Hash sum
    def sumK(self,root,k):
        # code here
        def helper(root,k,currSum,preSum):
            if root:
                currSum[0]+=root.data
                ans=preSum.get(currSum[0]-k,0)
                preSum[currSum[0]]=preSum.get(currSum[0],0)+1
                ans+=helper(root.left,k,currSum,preSum)
                ans+=helper(root.right,k,currSum,preSum)
                preSum[currSum[0]]-=1
                currSum[0]-=root.data
                return ans
            return 0
            
        currSum=[0]
        preSum={0:1}
        return helper(root,k,currSum,preSum)
    
    

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
    
    
    obj = Solution()

    print(obj.sumK_Bruteforce(root, k))
    
    print(obj.sumK(root, k))
    
