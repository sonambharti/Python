"""
Write a Python program to count all possible paths from top left to bottom right.
"""

# BruteForce Approach
# Using Recursion – O(2^(n+m)) Time and O(n+m) Space
def numberOfPaths_Brute(m, n):
    # If either given row number is first
    # or given column number is first
    if(m == 1 or n == 1):
        return 1

    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)

# Memoization Approach
# Using Top-Down DP (Memoization) – O(m*n) Time and O(m*n) Space
def numberOfPaths_memoization(m, n, memo):
    if n == 1 or m == 1:
        memo[m][n] = 1
        return 1

    # Add the element in the memo table
    # If it was not computed before
    if  memo[m][n] == 0:
         memo[m][n] = countPaths(m-1,n, memo) + \
            countPaths(m,n-1, memo)

    return  memo[m][n]

# Optimal DP Approach
# Using Space Optimized DP – O(n*m) Time and O(n) Space
def numberOfPaths(p, q):
    # Create a 1D array to store
    # results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    return dp[q - 1]

if __name__ == '__main__':
    m = 3
    n = 3
    res = numberOfPaths(m, n)
    print(res)
