'''
#   300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

def lengthOfLIS(nums):
    n = len(nums)
    maxwell = 1
    dp = [1] *n
    for i in range(n):
        for j in range(i):
            if(nums[i]>nums[j]):
                dp[i] = max(dp[i],dp[j]+1)
            maxwell = max(maxwell,dp[i])
    print(dp)
    return maxwell
    
    
if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    res = lengthOfLIS(nums)
    print("Length of Longest Increasing Subsequence: ", res)
