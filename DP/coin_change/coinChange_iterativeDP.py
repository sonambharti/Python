"""
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of 
money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""

def count_ways_to_make_sum(coins, amount):
    n = len(coins)
    INF = float('inf')

    # dp[i][j] = min coins to make amount j using first i coins
    dp = [[INF] * (amount + 1) for _ in range(n + 1)]

    # Base case: 0 coins needed to make amount 0
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the table
    for i in range(1, n + 1):  # i coins
        for j in range(1, amount + 1):  # amount j
            if coins[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][amount] if dp[n][amount] != INF else -1


# minm coins to make a amount using 1-D
def coinChange_DP(coin, amount):
  # Complexity = O(amount*len(coin))
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[amount] if dp[amount] != amount + 1 else -1
        

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    
    res = coinChange_DP(coins, amount)
    print(res)
    print("No. of ways to get the change using 2D: ", count_ways_to_make_sum(coins, amount))
