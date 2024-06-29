"""
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten.
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], 
[i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and 
(2,1) in unit time.

Example 2:

Input: grid = {{2,2,0,1}}
Output: -1
Explanation: The grid is-
2 2 0 1
Oranges at (0,0) and (0,1) can't rot orange at
(0,3).
"""

from collections import deque

def bfs(grid, sr, sc, nfresh, q):
    n = len(grid)
    m = len(grid[0])
    vis = [[False]*(m) for _ in range(n)]
    final_time = 0
    rfresh = 0
    while q:
        el = q.pop()
        sr = el[0][0]
        sc = el[0][1]
        lrow = [-1, 0, 1, 0]
        lcol = [0, -1, 0, 1]
        t = el[1]
        final_time = max(t, final_time)
        for k in range(4):
            curr_row = sr+lrow[k]
            curr_col = sc+lcol[k]
            
            if (0<=curr_row<n) and (0<=curr_col<m) and grid[curr_row][curr_col]==1 and vis[curr_row][curr_col]== False:
                rfresh += 1
                vis[curr_row][curr_col] = True
                q.appendleft([[curr_row, curr_col], t+1])
                
    if nfresh != rfresh:
        return -1
    return final_time
    
            
def orangesRotting(grid):
	#Code here
    n = len(grid)
    m = len(grid[0])
    q = deque()
    nfresh = 0
                    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.appendleft([[i, j], 0])
            if grid[i][j] == 1:
                nfresh += 1
                
                
    if q:
        el = q[0]
        sr = el[0]
        sc = el[1]
        res = bfs(grid, sr, sc, nfresh, q)
        return res
    return 0
		

if __name__ == "__main__":
    grid = [[0,1,2],[0,1,2],[2,1,1]]
    res = orangesRotting(grid)
    print("Total time to rotten all the oranges: ", res)
