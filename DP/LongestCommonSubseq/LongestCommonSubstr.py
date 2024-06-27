# Find the length of the common substrin of the given two strings...
"""
Substring: A Substring takes out characters from a string placed between two specified indices in a continuous order. 
Subsequence: A Subsequence can be derived from another sequence by deleting some or none of the elements in between 
but always maintaining the relative order of elements in the original sequence.
"""

def dp_LongestCommonSubstr(str1, str2, n, m):
    global dp
    max_length = 0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif str1[j-1] == str2[i-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0
            
    return max_length

if __name__ == "__main__":
    str1 = "abchiyp"
    str2 = "abpu"
    n = len(str1)
    m = len(str2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    
    res = dp_LongestCommonSubstr(str1, str2, n, m)
    print("Longest Common Substring: ", res)
    
