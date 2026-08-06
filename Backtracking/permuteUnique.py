'''
# 47. Permutations II 

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''
# Time Complexity: O(nlogn + n * n!)
# Space Complexity: O(n)
# Output Space: O(U * n)

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                # Skip duplicate numbers
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return res
        
if __name__ == "__main__":
    nums = [1,1,2]
    res = Solution().permuteUnique(nums)
    print(f"All the unique permutation of given array is: \n{res}")
