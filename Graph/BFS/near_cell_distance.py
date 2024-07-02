"""
# Distance of nearest cell having 1

Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges
Given a binary grid of n*m. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1  - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1. There should be atleast one 1 in the grid.
 

Example 1:

Input: grid = {{0,1,1,0},{1,1,0,0},{0,0,1,1}}
Output: {{1,0,0,1},{0,0,1,1},{1,1,0,0}}
Explanation: The grid is-
0 1 1 0 
1 1 0 0 
0 0 1 1 
0's at (0,0), (0,3), (1,2), (1,3), (2,0) and
(2,1) are at a distance of 1 from 1's at (0,1),
(0,2), (0,2), (2,3), (1,0) and (1,1)
respectively.
"""

from collections import deque

            
def near_cell_distance(grid):
	#Code here
    n = len(grid)
    m = len(grid[0])
    vis = [[False]*(m) for _ in range(n)]
    dist = [[0]*(m) for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                q.appendleft([[i, j], 0])
                vis[i][j] = True
	            
    while q:
        el = q.pop()
        sr = el[0][0]
        sc = el[0][1]
        step = el[1]
        lrow = [-1, 0, 1, 0]
        lcol = [0, -1, 0, 1]
        dist[sr][sc] = step
        for k in range(4):
            curr_row = sr+lrow[k]
            curr_col = sc+lcol[k]
            
            if (0<=curr_row<n) and (0<=curr_col<m) and vis[curr_row][curr_col]== False:
                vis[curr_row][curr_col] = True
                q.appendleft([[curr_row, curr_col], step+1])
    return dist
	

if __name__ == "__main__":
    grid = [[1,0,1],[1,1,0],[1,0,0]]
    res = near_cell_distance(grid)
    print("Total distance of nearest cell 1: ", res)
