"""
518. Coin Change II
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

def maxNoOfChange(amount, coins):
    n = len(coins)
    # Initialize the dp array
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    # If sum is 0, then answer is True (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the value in the bottom-right corner of the dp array
    return dp[n][amount]

if __name__ == "__main__":
    # Example usage
    coins = [1, 2, 5]
    amount = 11
    print(maxNoOfChange(coins, amount))  # Output: 3
