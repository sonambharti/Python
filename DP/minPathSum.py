'''
# 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''
  
import sys  
    
def rec_minPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    
    def helper(i, j, grid):
        if i == 0 and j == 0:
            return grid[0][0]
            
        if i < 0 or j < 0:
            return sys.maxsize
        
        up = grid[i][j] + helper(i-1, j, grid)
        left = grid[i][j] + helper(i, j-1, grid)

        minmSum = min(up, left)
        return minmSum
    
    # starting from right bottom corner
    return helper(n-1, m-1, grid)
    

# Optimized space Complexity
def minPathSum_tabular(grid):
    n = len(grid)
    m = len(grid[0])
    prev = [0]*m

    for i in range(n):
        curr = [0]*m
        for j in range(m):
            if i==0 and j == 0:
                curr[j] = grid[i][j]
            else:
                # Calculate the cost of moving up from the cell (i, j).
                up = grid[i][j]
                #  requiring prev j's col
                if i > 0:
                    up += prev[j]
                else:
                    # If we are at the top row and can't move up, set 'up' to a large value.
                    up += int(1e9)
                # Calculate the cost of moving left from the cell (i, j).
                left = grid[i][j]
                if j > 0:
                    left += curr[j-1]
                else:
                    # If we are at the leftmost column and can't move left, set 'left' to a large value.
                    left += int(1e9)
                # Store the minimum cost of reaching the current cell in dp[i][j].
                curr[j] = min(left, up)
                
        prev = curr

    return prev[m-1]
                


# Tabular Method
def minPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0]*(m) for _ in range(n)]
    

    for i in range(n):
        for j in range(m):
            if i==0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                # Calculate the cost of moving up from the cell (i, j).
                up = grid[i][j]
                #  requiring prev j's col
                if i > 0:
                    up += dp[i-1][j]
                else:
                    # If we are at the top row and can't move up, set 'up' to a large value.
                    up += int(1e9)
                # Calculate the cost of moving left from the cell (i, j).
                left = grid[i][j]
                if j > 0:
                    left += dp[i][j-1]
                else:
                    # If we are at the leftmost column and can't move left, set 'left' to a large value.
                    left += int(1e9)
                # Store the minimum cost of reaching the current cell in dp[i][j].
                dp[i][j] = min(up, left)

    return dp[n-1][m-1]
            

# Example usage:
if __name__ == "__main__":
    grid = [[9,4,9,9],[6,7,6,4],[8,3,3,7],[7,4,9,10]]
    
    print("Minm Path sum using recursion: ", rec_minPathSum(grid))
    print("Minm Path sum using Tabular: ", minPathSum_tabular(grid))
    print("Minm Path sum using space optimization: ", minPathSum(grid))
