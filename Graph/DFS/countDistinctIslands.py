"""
# No of Distinct Islands
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct 
islands where a group of connected 1s (horizontally or vertically) forms an island. 
Two islands are considered to be distinct if and only if one island is not equal to 
another (not rotated or reflected).

Example 1:

Input:
grid[][] = {{1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 0, 1, 1},
            {0, 0, 0, 1, 1}}
Output:
1
Explanation:
grid[][] = {{1, 1, 0, 0, 0}, 
            {1, 1, 0, 0, 0}, 
            {0, 0, 0, 1, 1}, 
            {0, 0, 0, 1, 1}}
Same colored islands are equal.
We have 2 equal islands, so we 
have only 1 distinct island.

"""

import sys
from typing import List
sys.setrecursionlimit(10**8)


def countDistinctIslands(grid):
    # code here
    n = len(grid)
    m = len(grid[0])
    vis = [[False]*m for _ in range(n)]
    dist_cords = []
    dist = set()

    lrow = [-1, 0, 1, 0]
    lcol = [0, -1, 0, 1]
    def dfs(grid, sr, sc, base_row, base_col):
        vis[sr][sc] = True
        dist_cords.append(tuple([sr-base_row, sc-base_col]))
        for k in range(4):
            curr_row = sr + lrow[k]
            curr_col = sc + lcol[k]
            if (0<=curr_row<n) and (0<=curr_col<m) and grid[curr_row][curr_col] == 1 and vis[curr_row][curr_col]==False:
                dfs(grid, curr_row, curr_col, base_row, base_col)
                
    
    for i in range(n):
        for j in range(m):
            if vis[i][j]==False and grid[i][j]==1:
                dist_cords = []
                base_row, base_col = i, j
                dfs(grid, i, j, base_row, base_col)
        
                dist_cords = tuple(dist_cords)
                dist.add(dist_cords)
    
    return len(dist)

if __name__ == "__main__":
    grid =  [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    print("No. of Distinct Islands: ", countDistinctIslands(grid))
