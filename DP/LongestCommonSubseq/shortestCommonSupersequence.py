"""
# Shortest Common Supersequence
Given two strings X and Y of lengths m and n respectively, 
find the length of the smallest string which has both, X and Y as its sub-sequences.
Note: X and Y can have both uppercase and lowercase letters.

Example 1

Input:
X = abcd, Y = xycd
Output: 6
Explanation: Shortest Common Supersequence
would be abxycd which is of length 6 and
has both the strings as its subsequences.
"""

def shortestCommonSupersequence(X, Y, m, n):
    #code here
    dp = [[-1]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    LCS_count = dp[m][n]
    return (m+n-LCS_count)
if __name__ == "__main__":
    str1 = "abpu"
    str2 = "abchiyp"
    m = len(str1)
    n = len(str2)
  
    res = shortestCommonSupersequence(str1, str2, m, n)
    print("Longest Common Subsequence: ", res)
