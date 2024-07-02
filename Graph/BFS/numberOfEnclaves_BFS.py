"""
# Number of Enclaves
You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or 
walking off the boundary of the grid.

Find the number of land cells in grid for which we cannot walk off the boundary of the grid in any 
number of moves.

Example 1:

Input:
grid[][] = {{0, 0, 0, 0},
            {1, 0, 1, 0},
            {0, 1, 1, 0},
            {0, 0, 0, 0}}
Output:
3
Explanation:
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
The highlighted cells represents the land cells.
"""


from collections import deque

def numberOfEnclaves(grid):
    # code here
    n = len(grid)
    m = len(grid[0])
    vis =[[False]*m for _ in range(n)]
    total_land_count = 0
    q = deque()
    
    for i in range(n):
        if grid[i][0]==1 and vis[i][0]==False:
            q.appendleft([i, 0])
        if grid[i][m-1]==1 and vis[i][m-1]==False:
            q.appendleft([i, m-1])
            
    for j in range(m):
        if grid[0][j]==1 and vis[0][j]==False:
             q.appendleft([0, j])
        if grid[n-1][j]==1 and vis[n-1][j]==False:
            q.appendleft([n-1, j])
            
    lrow = [-1, 0, 1, 0]
    lcol = [0, -1, 0, 1]
    while q:
        el = q.pop()
        sr = el[0]
        sc = el[1]
        vis[sr][sc] = True
        for i in range(4): 
            curr_row = sr+lrow[i]
            curr_col = sc+lcol[i]
            if (0<=curr_row<n) and (0<=curr_col<m)and grid[curr_row][curr_col]==1 and vis[curr_row][curr_col] == False:
                q.appendleft([curr_row, curr_col])
                
    for i in range(n):
        for j in range(m):
            if vis[i][j]==False and grid[i][j]==1:
                total_land_count += 1
    return total_land_count

if __name__ == "__main__":
    
    grid = [[0, 0, 0, 0], 
       [1, 0, 1, 0], 
       [0, 1, 1, 0],  
       [0, 0, 0, 0]]
    res = numberOfEnclaves(grid)
    print("No of land encalaves which is connected to boundary", res)
