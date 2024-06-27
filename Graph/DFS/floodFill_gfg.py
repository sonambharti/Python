"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image.

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel 
value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the 
starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those 
pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the 
aforementioned pixels with the newColor.

Examples:

Input: image = {{1,1,1},{1,1,0},{1,0,1}},
sr = 1, sc = 1, newColor = 2.
Output: {{2,2,2},{2,2,0},{2,0,1}}
Explanation: From the center of the image (with position (sr, sc) = (1, 1)), all pixels 
connected by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
"""

def floodFill(image, sr, sc, newColor):
    #Code here
	res = image
	n = len(res)
	m = len(res[0])
	vis =[[False]*m for _ in range(n)]
	oldColor = image[sr][sc]
	def dfs(res, sr, sc, newColor):
	    lrow = [0, -1, 0, 1, 0]
	    lcol = [0, 0, -1, 0, 1]
	    for i in range(5): 
	        curr_row = sr+lrow[i]
	        curr_col = sc+lcol[i]
	        if (0<=curr_row<n) and (0<=curr_col<m)and res[curr_row][curr_col]==oldColor and vis[curr_row][curr_col] == False:
	            vis[curr_row][curr_col] = True
	            res[curr_row][curr_col] = newColor
	            dfs(image, curr_row, curr_col, newColor)
	dfs(res, sr, sc, newColor)
	return res
	
if __name__ == "__main__":
    sr = 1 
    sc = 1 
    newColor = 2
    image = [[1,1,1],[1,1,0],[1,0,1]]
    res = floodFill(image, sr, sc, newColor)
    print("New Image Board:\n", res)
    
    
