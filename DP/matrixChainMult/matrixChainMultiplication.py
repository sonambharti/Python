# Minimum Score Triangulation of Polynomial
"""
You have a convex n-sided polygon where each vertex has an integer value. 
You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, 
the value of that triangle is the product of the values of its vertices, and 
the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

"""

MOD = 10**9+7
dp = []
arr = []

def matrixChainMul(i, j):
    
    if i==j:
        return 0
        
    if dp[i][j] != -1:
        return dp[i][j]
        
    dp[i][j] = MOD
    
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrixChainMul(i, k) + matrixChainMul(k+1, j) + arr[i-1] * arr[k] * arr[j])
    
    return dp[i][j]
    
    
if __name__ == "__main__":
    
    arr = [10, 20, 30, 40, 30]
    n = len(arr)
    
    dp = [[-1]*n for _ in range(n)]
    
    res = matrixChainMul(1, n-1)
    print("Minimum number of multiplications is: ", res)
