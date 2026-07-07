"""
# 1293. Shortest Path in a Grid with Obstacles Elimination

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, 
left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. 
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Example 2:
Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
Output: -1
Explanation: We need to eliminate at least two obstacles to find such a walk.

"""

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        obstacles = [[float('inf')]*m for _ in range(n)]
        q = deque([[0,0,0,0]]) # insert [row, column, obstacles, steps]
        obstacles[0][0] = 0
        count = 0
        while q:
            node = q.pop()
            print(f"node = {node}, type = {type(node)}")
            row, col, obs, steps = node[0], node[1], node[2], node[3]

            if row == n-1 and col == m-1:
                return steps

            lrow = [-1, 0, 1, 0]
            lcol = [0, 1, 0, -1]

            for i in range(4):
                curr_row = lrow[i] + row
                curr_col = lcol[i] + col
                if (0<=curr_row<n) and (0<=curr_col<m):
                    new_obs = obstacles[row][col] + grid[curr_row][curr_col]
                    if new_obs < obstacles[curr_row][curr_col] and new_obs <= k:
                        obstacles[curr_row][curr_col] = new_obs
                        q.appendleft([curr_row, curr_col, obstacles[curr_row][curr_col], steps + 1])
        
        return -1
        
if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]] 
    k = 1
    
    res = Solution().shortestPath(grid, k)
    print(res)

