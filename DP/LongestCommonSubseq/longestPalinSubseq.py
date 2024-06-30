"""
# Longest Palindromic Subsequence
Given a String, find the longest palindromic subsequence.

NOTE: Subsequence of a given sequence is a sequence that can be derived from the given 
sequence by deleting some or no elements without changing the order of the remaining elements

Example 1:

Input:
S = "bbabcbcab"
Output: 7
Explanation: Subsequence "babcbab" is the
longest subsequence which is also a palindrome.
"""

def longestPalinSubseq(S):
    # code here
    n  = len(S)
    rev_S = S[::-1]
    dp = [[-1]*(n+1) for _ in range(n+1)]
	
    for i in range(n+1):
        for j in range(n+1):
	        if (i==0 or j==0):
	            dp[i][j] = 0
	        elif S[i-1] == rev_S[j-1]:
	            dp[i][j] = 1 + dp[i-1][j-1]
	        else:
	            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	            
    return dp[n][n]
    
    
if __name__ == "__main__":
    str1 = "bbabcbcab"
    res = longestPalinSubseq(str1)
    print("Longest Palindromic Subsequence: ", res)
