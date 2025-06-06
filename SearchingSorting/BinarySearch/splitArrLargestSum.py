'''
# 410. Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum 
of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 
Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
'''

from typing import List 

class Solution:
    def isPossible(self, arr, maxmSum, k):
        count = 1
        minm_sum = 0
        for i in range(len(arr)):
            minm_sum += arr[i]
            if minm_sum > maxmSum:
                count += 1
                minm_sum = arr[i]
        return count <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        summ = 0
        maxm = 0

        for i in range(n):
            summ += nums[i]
            maxm = max(maxm, nums[i])
        
        low = maxm
        high = summ
        ans = high

        while(low <= high):
            mid = low + (high - low) // 2
            if self.isPossible(nums, mid, k): # if any soln is possible for the given sum
                ans = min(ans, mid) # find minm of largest sum
                high = mid - 1
            else:
                low = mid + 1
        return ans

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    k = 2
    
    obj = Solution()
    res = obj.splitArray(nums, k)
    print(res)
    
