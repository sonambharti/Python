"""
# 132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

"""
MOD = 10**9+7

def minCutMatrixMult(s):
    n = len(s)
    dp = [-1]*(n+1)
    def is_palindrome(string, i, j):
        if i>= j:
            return True
        while i<j:
            if string[i]!=string[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def rec_palindromicPartition(string, i, j):
        global MOD
        if i>=j or is_palindrome(string, i, j) == True:
            dp[i] = 0

        if dp[i] != -1:
            return dp[i]
            
        dp[i] = MOD
        for k in range(i, j):
            if is_palindrome(string, i, k):
                if dp[k+1] != -1:
                    right = dp[k+1]
                else:
                    right = rec_palindromicPartition(string, k+1, j)
                    dp[k+1] = right
                dp[i] = min(dp[i], 1 + right)
        return dp[i]
    return rec_palindromicPartition(s, 0, n-1)

def minCutPalindromic(s):

    n = len(s)
    dp = [[-1] * n for _ in range(n)]
    P = [[False] * n for _ in range(n)]
    
    # Every substring of length 1 is a palindrome
    for i in range(n):
        P[i][i] = True
    
    # L is substring length. Build the solution in a bottom-up manner
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if L == 2:
                P[i][j] = (s[i] == s[j])
            else:
                P[i][j] = (s[i] == s[j]) and P[i + 1][j - 1]

    # Fill the dp table for the minimum cuts
    for i in range(n):
        if P[0][i]:
            dp[0][i] = 0
        else:
            dp[0][i] = MOD
            for j in range(i):
                if P[j + 1][i] and dp[0][j] + 1 < dp[0][i]:
                    dp[0][i] = dp[0][j] + 1
    
    return dp[0][n - 1]
    
if __name__ == "__main__":
    s = "aab"
    res1 = minCutMatrixMult(s)
    print("All possible palindrome partitioning of s using Matrix Multiplication: ", res1)
    res2 = minCutPalindromic(s)
    print("All possible palindrome partitioning of s: ", res2)
