"""
Given an array arr[] of size N, check if it can be partitioned into two parts 
such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation: 
The two parts are {1, 5, 5} and {11}.
"""
def equalPartition(N, arr):
    # code here
    def isSubsetSum(arr, n, sumn):
        # Initialize the dp array
        dp = [[False] * (sumn + 1) for _ in range(n + 1)]
    
        # If sum is 0, then answer is True (empty subset)
        for i in range(n + 1):
            dp[i][0] = True
    
        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(1, sumn + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
    
        # Return the value in the bottom-right corner of the dp array
        return dp[n][sumn]
        
    sumn = 0
    for i in arr:
        sumn += i
    if sumn%2 != 0:
        return False
    else:
        return isSubsetSum(arr, N, sumn//2)
        
if __name__ == "__main__":
  # Example usage
  arr = [3, 34, 4, 12, 5, 2]
  
  n = len(arr)
  print(equalPartition(n, arr))
