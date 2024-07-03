"""
# Sequence Pattern Matching
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

def isSubsequence(s,t):
    n = len(t)
    m = len(s)
    dp = [[-1]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    LCS_len = dp[m][n]
    
    if LCS_len == m:
        return True
    return False
    
    
if __name__ == "__main__":
    s = "abc" 
    t = "ahbgdc"
    res = isSubsequence(s,t)
    print("Is s Subsequence of t: ", res)
