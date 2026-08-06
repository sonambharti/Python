'''
# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

'''
# Time Complexity: O(n * n!)
# Space Complexity: O(n)
# Output Space: O(n * n!)
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            # Base case
            if len(path) == len(nums):
                res.append(path[:]) # path[:] stores the copy of path instead of it's reference
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return res
        
        
        
if __name__ == "__main__":
    nums = [1,2, 3]
    res = Solution().permute(nums)
    print(f"All the permutation of given array is: \n{res}")
