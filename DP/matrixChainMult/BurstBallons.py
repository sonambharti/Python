"""
# 312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number 
on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon 
with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
"""

def maxCoins(nums):
        
    N = len(nums)
    nums = [1] + nums + [1]
    dp = [[-1]*(N+1) for _ in range(N+1)]
    
    def rec_chainMatMult(nums, i, j):
        if i>j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
            
        MOD = -10**9+7
        dp[i][j] = MOD
        for k in range(i, j+1):
            dp[i][j] = max(dp[i][j], rec_chainMatMult(nums, i, k-1) + 
            rec_chainMatMult(nums, k+1, j) + nums[i-1]*nums[k]*nums[j+1])
           
        return dp[i][j]
    return rec_chainMatMult(nums, 1, N)
        
    
if __name__ == "__main__":
    nums = [3,1,5,8]
    res = maxCoins(nums)
    print("Maximum Coins collected = ", res)
