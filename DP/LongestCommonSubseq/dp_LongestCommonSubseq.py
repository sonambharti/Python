# Find the length of the common subsequece of the given two strings...

def rec_LongestCommonSubseq(str1, str2, n, m):
    if n==0 or m==0:
        return 0
        
    elif str1[n-1] == str2[m-1]:
        return 1+rec_LongestCommonSubseq( str1, str2, n-1, m-1)
    else:
        return max(rec_LongestCommonSubseq(str1, str2, n-1, m), rec_LongestCommonSubseq(str1, str2, n, m-1))
        
        
# Using memoization dp (bottom-up approach)   
dp = []
def memoization_LongestCommonSubseq(str1, str2, n, m):
    global dp
    if n==0 or m==0:
        return 0
    elif dp[m][n] != -1:
        return dp[m][n]
    elif str1[n-1] == str2[m-1]:
        dp[m][n] = 1+memoization_LongestCommonSubseq( str1, str2, n-1, m-1)
    else:
        dp[m][n] = max(memoization_LongestCommonSubseq(str1, str2, n-1, m), memoization_LongestCommonSubseq(str1, str2, n, m-1))
        
    return dp[m][n]

def dp_LongestCommonSubseq(str1, str2, n, m):
    global dp
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            
            elif str1[j-1] == str2[i-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
    return dp[m][n]

if __name__ == "__main__":
    str1 = "abchiyp"
    str2 = "abpu"
    n = len(str1)
    m = len(str2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    
    # res = rec_LongestCommonSubseq(str1, str2, n, m)
    # res = memoization_LongestCommonSubseq(str1, str2, n, m)
    res = dp_LongestCommonSubseq(str1, str2, n, m)
    print("Longest Common Subsequence: ", res)
    
