'''
# 1020. Number of Enclaves

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary 
of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.

'''

from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[False]*m for _ in range(n)]
        
        total_count = 0

        def dfs(grid, sr, sc):
            lr = [-1, 0, 1, 0]
            lc = [0, -1, 0, 1]
            vis[sr][sc] = True
            for i in range(4):
                curr_row = sr + lr[i]
                curr_col = sc + lc[i]
                if (0<=curr_row<n) and (0<=curr_col<m) and (grid[curr_row][curr_col] == 1) and (vis[curr_row][curr_col] == False):
                    dfs(grid, curr_row, curr_col)

        
        for i in range(n):
            if grid[i][0] == 1 and vis[i][0] == False:
                dfs(grid, i, 0)
            if grid[i][m-1] == 1 and vis[i][m-1] == False:
                dfs(grid, i, m-1)
        
        for j in range(m):
            if grid[0][j] == 1 and vis[0][j] == False:
                dfs(grid, 0, j)
            if grid[n-1][j] == 1 and vis[n-1][j] == False:
                dfs(grid, n-1, j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == False:
                    total_count += 1

        return total_count
        
        
if __name__ == "__main__":
    # grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    res = Solution().numEnclaves(grid)
    print(f"Number of land cells in grid for which we cannot walk off the boundary is: {res}")
