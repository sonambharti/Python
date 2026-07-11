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

        q = deque()

        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j] == 1:
                        q.append([i, j])
                        vis[i][j] = True

        lr = [-1, 0, 1, 0]
        lc = [0, -1, 0, 1]
        while q:
            sr, sc = q.pop()
            for i in range(4):
                curr_row = sr + lr[i]
                curr_col = sc + lc[i]
                if (0<=curr_row<n) and (0<=curr_col<m) and (grid[curr_row][curr_col] == 1) and (vis[curr_row][curr_col] == False):
                    q.append([curr_row, curr_col])
                    vis[curr_row][curr_col] = True

        for i in range(n):
            for j in range(m):
                if vis[i][j]==False and grid[i][j] == 1:
                    total_count += 1

        return total_count
        
        
if __name__ == "__main__":
    # grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    res = Solution().numEnclaves(grid)
    print(f"Number of land cells in grid for which we cannot walk off the boundary is: {res}")
