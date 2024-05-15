"""
Subset Sum Problem -> GFG

Given an array of non-negative integers, and a value sum, 
determine if there is a subset of the given set with sum equal to given sum. 


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
"""

def isSubsetSum(arr, n, sum):
    # Initialize the dp array
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is True (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the value in the bottom-right corner of the dp array
    return dp[n][sum]

if __name__ == "__main__":
  # Example usage
  arr = [3, 34, 4, 12, 5, 2]
  sum_value = 9
  n = len(arr)
  if isSubsetSum(arr, n, sum_value):
      print(1)
  else:
      print(0)
