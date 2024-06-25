"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque
def numIslands(grid):
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
            lrow = [-1,0,1,0]
            lcol = [0,-1,0,1]
            for i in range(4): 
                curr_row = row+lrow[i]
                curr_col = col+lcol[i]
                if (0<=curr_row<n) and (0<=curr_col<m)and grid[curr_row][curr_col]=="1" and vis[curr_row][curr_col] == False:
                    vis[curr_row][curr_col] = True
                    q.appendleft([curr_row, curr_col])
            

    for i in range(n):
        for j in range(m):
            if vis[i][j] == False and grid[i][j]=="1":
                bfs(grid, [i,j], n, m)
                count += 1
    return count
    

if __name__ == "__main__":
    grid = [["1","1","1","1","0"],
              ["1","1","0","1","0"],
              ["1","1","0","0","0"],
              ["0","0","0","0","0"]]
    res = numIslands(grid)
    print("No of islands = ", res)
