"""
# Longest Repeating Subsequence
Given string str, find the length of the longest repeating subsequence such that 
it can be found twice in the given string.

The two identified subsequences A and B can use the same ith character from string 
str if and only if that ith character has different indices in A and B. 
For example, A = "xax" and B = "xax" then the index of first "x" must be different 
in the original string for A and B.

Example 1:

Input:
str = "axxzxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x z x y 
0 1 2 3 4 5

The longest subsequence is "xx". 
It appears twice as explained below.
"""

def LongestRepeatingSubsequence(str1):
	# Code here
    n =len(str1)
    str2 = str1
    m= len(str2)
    dp = [[-1]*(m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if (i==0 or j==0):
                dp[i][j] = 0
            elif (str1[i-1] == str2[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
    
    
if __name__ == "__main__":
    str1 = "bbabcbcab"
    res = LongestRepeatingSubsequence(str1)
    print("Longest Repeating Subsequence: ", res)
