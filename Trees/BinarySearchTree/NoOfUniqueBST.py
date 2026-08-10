'''
# 96. Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.

 

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1

'''


class Solution:
    def numTrees(self, n: int) -> int:
        # numTrees[4] = numTree[0] * numTree[3] + 
        #               numTree[1] * numTree[2] +
        #               numTree[2] * numTree[1] +
        #               numTree[3] * numTree[0] 
        #           = 5 + 2 + 2 + 5
        numTree = [1] * (n + 1)
        # 0 nodes = 1 tree
        # 1 nodes = 1 tree
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]
        
if __name__ == "__main__":
    n = 4
    res = Solution().numTrees(n)
    print(f"Possible unique BST from n nodes are: {res}")
