"""
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that 
amount of money cannot be made up by any combination of the coins, return 0.

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

dp = []
def maxWays_coinChange_tabularDP(coins, amount, n):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if n <= 0 and amount > 0:
        return 0

    if dp[n][amount] != -1:
        return dp[n][amount]
        
    dp[n][amount] = maxWays_coinChange_tabularDP(coins, amount, n-1) + maxWays_coinChange_tabularDP(coins, amount-coins[n-1], n) 

    return dp[n][amount]


if __name__ == "__main__":  
    coins = [1,2,3]
    amount = 6
    n = len(coins)
    dp = [[-1]*(amount+1) for i in range(n+1)]
    res = maxWays_coinChange_tabularDP(coins, amount, n)
    print(res)
