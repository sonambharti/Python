"""
# Optimal Strategy For A Game

You are given an array arr of size n. The elements of the array represent n coin of values v1, v2, ....vn. 
You play against an opponent in an alternating way. In each turn, a player selects either the first or 
last coin from the row, removes it from the row permanently, and receives the value of the coin.
You need to determine the maximum possible amount of money you can win if you go first.
Note: Both the players are playing optimally.

Example 1:

Input:
n = 4
arr[] = {5, 3, 7, 10}
Output: 
15
Explanation: The user collects maximum
value as 15(10 + 5). It is guarantee that we cannot get more than 15 by any possible moves.
"""
def dfs(left, right, arr, dp):
    if left > right:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]
    takeLeft = arr[left] + min(dfs(left+2, right, arr, dp), dfs(left+1, right-1, arr, dp))
    takeRight = arr[right] + min(dfs(left+1, right-1, arr, dp), dfs(left, right-2, arr, dp))
    dp[left][right] = max(takeLeft, takeRight)
    return dp[left][right]
    
def optimalStrategyOfGame(n, arr):
    # code here
    dp = [[-1]*(n+1) for _ in range(n+1)]
    return dfs(0, n-1, arr, dp)
        

if __name__ == "__main__":
    # Example usage and comparison of approaches
    
    n = 4
    arr = [5, 3, 7, 10]
    
    print("Optimal Strategy Of Game")
    print("the maximum possible amount of money you can win if you go first: ", optimalStrategyOfGame(n, arr))
