'''
#   417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches 
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
north, south, east, and west if the neighboring cell's height is less than or equal to the 
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
'''


def pacificAtlantic(heights):
    rows = len(heights)
    cols = len(heights[0])

    pacific_visited = set()
    atlantic_visited = set()

    def dfs(visited, row, col, start_value):
        #   check grid boundaries
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        
        #   cell has been visited
        if(row, col) in visited:
            return
        
        #   check condition
        if heights[row][col] < start_value:
            return
        
        visited.add((row, col))
    
        #   check all 4-directions
        dfs(visited, row+1, col, heights[row][col])
        dfs(visited, row-1, col, heights[row][col])
        dfs(visited, row, col+1, heights[row][col])
        dfs(visited, row, col-1, heights[row][col])

    for col in range(cols):
        dfs(pacific_visited, 0, col, heights[0][col]) # top row
        dfs(atlantic_visited, rows-1, col, heights[rows-1][col]) # bottom row
    
    for row in range(rows):
        dfs(pacific_visited, row, 0, heights[row][0]) # 1st col
        dfs(atlantic_visited, row, cols-1, heights[row][cols-1]) # last col

    #find the cells that are in both sets
    output = [list(cell) for cell in pacific_visited & atlantic_visited]

    return output
            
    
    
if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    res = pacificAtlantic(heights)
    print("Pacific Atlantic Water Flow: ", res)
