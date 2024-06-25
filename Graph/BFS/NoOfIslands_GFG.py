"""
# GFG -> No. of Islands Practice

Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). 
Find the number of islands.

Note: An island is either surrounded by water or boundary of grid and is formed by connecting 
adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.
"""

from collections import deque

def numIslands(grid):
    #code here
    n = len(grid)
    m = len(grid[0])
    vis = [[False]*m for _ in range(n)]
    count = 0
    def bfs(grid, node, n, m):
        vis[node[0]][node[1]] = True
        q = deque([node])
        while q:
            el = q.pop()
            row, col = el[0], el[1]
            for i in range(-1,2): 
                for j in range(-1,2):
                    curr_row = row+i
                    curr_col = col+j
                    if (0<=curr_row<n) and (0<=curr_col<m) and grid[curr_row][curr_col]==1 and vis[curr_row][curr_col] == False:
                        vis[curr_row][curr_col] = True
                        q.appendleft([curr_row, curr_col])
            

    for i in range(n):
        for j in range(m):
            if (vis[i][j] == False and grid[i][j]==1):
                count += 1
                bfs(grid, [i,j], n, m)
    return count
    

if __name__ == "__main__":
    grid = [[0, 1],[1, 0],[1, 1],[1, 0]]
    res = numIslands(grid)
    print("No of islands = ", res)
