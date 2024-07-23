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

def minCutMatrixMult(string):
    # code here
    n = len(string)
    dp = [[-1]*(n) for _ in range(n)]
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
        if i>=j:
            dp[i][j] = 0
        if is_palindrome(string, i, j) == True:
            dp[i][j] = 0
        if dp[i][j] != -1:
            return dp[i][j]
            
        dp[i][j] = MOD
        for k in range(i, j):
            # minm_part = min(minm_part, 1 + rec_palindromicPartition(string, i, k) + rec_palindromicPartition(string, k+1, j))
            if dp[i][k] != -1:
                left = dp[i][k]
            else:
                left = rec_palindromicPartition(string, i, k)
                dp[i][k] = left
            if dp[k+1][j] != -1:
                right = dp[k+1][j]
            else:
                right = rec_palindromicPartition(string, k+1, j)
                dp[k+1][j] = right
            dp[i][j] = min(dp[i][j], 1 + left + right)
        return dp[i][j]
    return rec_palindromicPartition(string, 0, n-1)
        
def minCutPalindromic(s):

    n = len(s)
    dp = [-1] * n
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
            dp[i] = 0
        else:
            dp[i] = MOD
            for j in range(i):
                if P[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
                    
    print("Palindrome Table:\n")
    for i in range(n):
        print(P[i])
    print("\n-----------------------------------\n")
    print("DP Table:\n")
    print(dp)
    
    return dp[n - 1]
    
if __name__ == "__main__":
    s = "aabackca"
    res1 = minCutMatrixMult(s)
    print("All possible palindrome partitioning of s using Matrix Multiplication: ", res1)
    res2 = minCutPalindromic(s)
    print("All possible palindrome partitioning of s: ", res2)
