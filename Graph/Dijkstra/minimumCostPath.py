'''
# Minimum Cost Path

Given a square grid of size N, each cell of which contains an integer cost that 
represents a cost to traverse through that cell, we need to find a path from the 
top left cell to the bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).  

Examples :

Input: grid = {{9,4,9,9},{6,7,6,4},{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.
Input: grid = {{4,4},{3,7}}
Output: 14
Explanation: The grid is-
4 4
3 7
The minimum cost is- 4 + 3 + 7 = 14.
 
'''
    
import heapq

def minimumCostPath(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Priority queue for Dijkstra's algorithm
    pq = [(grid[0][0], 0, 0)]  # (cost, row, col)
    
    # Distance array to keep track of the minimum cost to reach each cell
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = grid[0][0]
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        
        # If we've reached the bottom-right corner, return the cost
        if x == n - 1 and y == m - 1:
            return cost
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_cost = cost + grid[nx][ny]
                
                # If we find a cheaper way to get to (nx, ny), update and push to the priority queue
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny))
    
    return dist[n-1][m-1]
    


# Example usage:
if __name__ == "__main__":
    grid = [[9,4,9,9],[6,7,6,4],[8,3,3,7],[7,4,9,10]]
    print(minimumCostPath(grid))
