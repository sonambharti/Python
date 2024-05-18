"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""
import sys, math
def countTargetDifferenceSubsetSum(nums, n, target):
    def countSubsetSum(arr, n, sumn):
        # Initialize the dp array
        dp = [[0] * (sumn + 1) for _ in range(n + 1)]
        # If sum is 0, then answer is True (empty subset)
        for i in range(n + 1):
            dp[i][0] = 1
    
        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(0, sumn + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - arr[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
    
        # Return the value in the bottom-right corner of the dp array
        return dp[n][sumn]

    n = len(nums)
    sume = sum(nums)
    
    # Check if target + sume is even and non-negative
    if (sume + target) % 2 != 0 or sume < abs(target):
        return 0
    
    s1 = (sume + target) // 2
    return countSubsetSum(nums, n, s1)
   
        
if __name__ == "__main__":
  # Example usage
  arr = [1,1,1,1,1]
  n = len(arr)
  target = 3
  print(countTargetDifferenceSubsetSum(arr, n, target))
