"""
**Subsequence** - A sequence obtained from an original string/list which are common to the other string/list by 
                  removing the middle elements in the same order. 
                  A subsequence maintain relative ordering of elements but may or may not be a contiguous part of an array.
"""

def LCS(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0]*(n+1) for i in range(m+1)]
    
    for i in range(0, m):
        for j in range(0,n):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
    # read the LCS from the dp
    LCS = []
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            LCS.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    LCS = LCS[::-1]
    return LCS


if __name__ == '__main__':
    S1 = "Paranormal"
    S2 = "Parthanoma"
    res = LCS(S1, S2)
    print ("Length of LCS is: ", len(res))
    print("Longest sequence is: ", res)
