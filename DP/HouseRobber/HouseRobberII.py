'''
# 213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain 
amount of money stashed. All houses at this place are arranged in a circle. That means the 
first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system 
connected, and it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum 
amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are
adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
'''

from typing import List

# dp method Time Complexity - O(n) and Space Complexity - O(2n)
def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[1] = nums[0]
    dp2[1] = nums[n-1]
    for i in range(2, n):
        dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i-1])
        dp2[i] = max(dp2[i-1], dp2[i-2]+nums[n-i])
    return max(dp1[-1], dp2[-1])


#   Optimized method Time Complexity - O(n) and Space Complexity - O(1)
def rob_optimized(nums: List[int]) -> int:
    def helper(nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    return max(helper(nums[1:]), helper(nums[:-1]))

        


if __name__ == "__main__":
    # nums = [1,2,3]
    nums = [2,3,2]
    print(f"the maximum amount of money you can rob tonight without alerting the police: {rob(nums)}")
    
    print(f"the optimized maximum amount of money you can rob tonight without alerting the police: {rob_optimized(nums)}")
