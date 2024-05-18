"""
Count subset sum using dp
similar to 0-1 knapsack 
"""

def countSubsetSum(arr, n, sumn):
    # Initialize the dp array
    dp = [[0] * (sumn + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is True (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, sumn + 1):
            if arr[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - arr[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the value in the bottom-right corner of the dp array
    return dp[n][sumn]
    
   
        
if __name__ == "__main__":
  # Example usage
  arr = [3, 24, 4, 12, 5, 2]
  target = 24
  n = len(arr)
  print(countSubsetSum(arr, n, target))
