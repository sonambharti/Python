"""
# Minimum Points To Reach Destination

Given a m*n grid with each cell consisting of positive, negative, or zero point.
We can move across a cell only if we have positive points. Whenever we pass 
through a cell, points in that cell are added to our overall points, the task is to 
find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
1. From a cell (i, j) we can move to (i + 1, j) or (i, j + 1).
2. We cannot move from (i, j) if your overall points at (i, j) are <= 0.
3. We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.

Example 1:

Input: 
m = 3, n = 3 
points = {{-2,-3,3}, 
          {-5,-10,1},
          {10,30,-5}} 
Output: 
7 
"""
# Brute Force Approach
def minPointsBruteForce(points):
    m, n = len(points), len(points[0])
    
    # Define a recursive function to explore all possible paths
    def backtrack(i, j, current_points):
        # Base case: if the frog reaches the last cell, return the minimum initial points required
        if i == m - 1 and j == n - 1:
            return max(1, 1 - current_points)
        # Calculate the points earned by moving to the right cell
        right_points = backtrack(i, j + 1, current_points + points[i][j + 1]) if j + 1 < n else float('inf')
        # Calculate the points earned by moving to the bottom cell
        bottom_points = backtrack(i + 1, j, current_points + points[i + 1][j]) if i + 1 < m else float('inf')
        # Return the minimum initial points required to reach the last cell
        return max(1, min(right_points, bottom_points) - current_points)
    
    # Start exploring all possible paths from the first cell
    return backtrack(0, 0, points[0][0])

# Dynamic Programming Approach
def minPointsDP(points):
    m, n = len(points), len(points[0])
    # Initialize a 2D DP array to store the minimum initial points required to reach each cell
    dp = [[float('inf')] * n for _ in range(m)]
    # Calculate the minimum initial points required to reach the last cell using dynamic programming
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = max(1, 1 - points[i][j])
            else:
                right_points = dp[i][j + 1] if j + 1 < n else float('inf')
                bottom_points = dp[i + 1][j] if i + 1 < m else float('inf')
                dp[i][j] = max(1, min(right_points, bottom_points) - points[i][j])
    # The minimum initial points required to reach the last cell is stored in dp[0][0]
    return dp[0][0]


    
if __name__ == "__main__":
    # Example usage and comparison of approaches
    points = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    # Brute Force Approach
    print("Brute Force Approach:")
    print("Minimum initial points required:", minPointsBruteForce(points))
    # Dynamic Programming Approach
    print("Dynamic Programming Approach:")
    print("Minimum initial points required:", minPointsDP(points))
