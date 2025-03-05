"""
# 131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a 
palindrome. Return all possible palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""
def partitionPalindromicSubstr(s):
    n = len(s)
    
    # Precompute the palindrome table
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True  # Every single character is a palindrome
    
    for length in range(2, n + 1):  # Substring lengths from 2 to n
        for start in range(n - length + 1):
            end = start + length - 1
            if length == 2:
                dp[start][end] = (s[start] == s[end])
            else:
                dp[start][end] = (s[start] == s[end]) and dp[start + 1][end - 1]

    def backtrack(start):
        if start == n:
            result.append(current_partition[:])
            return
        
        for end in range(start, n):
            if dp[start][end]:
                current_partition.append(s[start:end + 1])
                backtrack(end + 1)
                current_partition.pop()
    
    result = []
    current_partition = []
    backtrack(0)
    return result
    
if __name__ == "__main__":
    s = "aab"
    res = partitionPalindromicSubstr(s)
    print("All possible palindrome partitioning of s: ", res)
