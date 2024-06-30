"""
# 583. Delete Operation for Two Strings => Leetcode
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""

def minDistance(word1, word2):
    n  = len(word1)
    m = len(word2)
    dp = [[-1]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
	        if (i==0 or j==0):
	            dp[i][j] = 0
	        elif word1[i-1] == word2[j-1]:
	            dp[i][j] = 1 + dp[i-1][j-1]
	        else:
	            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    del1 = n-dp[n][m]
    del2 = m-dp[n][m]
	            
    return (del1+del2)
    
if __name__ == "__main__":
    word1 = "sea"
    word2 = "eat"
    
    res = minDistance(word1, word2)
    print("No of deletion: ", res)
