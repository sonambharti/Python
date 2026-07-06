"""
# 733. Flood Fill

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value
of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image 
starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it 
matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of 
the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]

Explanation:
The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.
"""

from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        oldColor = image[sr][sc]
        vis = [[False]*m for _ in range(n)]

        def bfs(res, color):
            vis[sr][sc] = True
            image[sr][sc] = color
            q = deque([[sr, sc]])

            while q:
                el = q.pop()
                row, col = el[0], el[1]
                lrow = [0, -1, 0, 1, 0]
                lcol = [0, 0, 1, 0, -1]

                for i in range(5):
                    curr_row = row + lrow[i]
                    curr_col = col + lcol[i]
                    if (0<=curr_row<n) and (0<=curr_col<m) and image[curr_row][curr_col]==oldColor and not vis[curr_row][curr_col]:
                        image[curr_row][curr_col] = color
                        vis[curr_row][curr_col] = True
                        q.appendleft([curr_row, curr_col])
        
        bfs(image, color)

if __name__ == "__main__":
    image = [[1,1,1],[1,1,0],[1,0,1]] 
    sr = 1
    sc = 1
    color = 2
    
    Solution().floodFill(image, sr, sc, color)
    print(image)
