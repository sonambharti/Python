'''
# Count Paths with the given XOR value

You are given a 2D integer array grid with size m x n. You are also given an integer k.

Your task is to calculate the number of paths you can take from the top-left cell (0, 0) to the 
bottom-right cell (m - 1, n - 1) satisfying the following constraints:

You can either move to the right or down. Formally, from the cell (i, j) you may move to the cell 
(i, j + 1) or to the cell (i + 1, j) if the target cell exists.
The XOR of all the numbers on the path must be equal to k.
Return the total number of such paths.

Since the answer can be very large, return the result modulo 109 + 7.

Example 1:

Input: grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11

Output: 3


'''

def countPathsWithXORValue(grid, k):
    # Time Complexity: O(n.m.X) -> X - range of the xor
    # Space Complexity: O(n.m.X)
    
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])

    # Memoization table for DP: dp[x][y][xor_value]
    dp = {}

    def dfs(x, y, xor_value):
        # Base case: if we reach the bottom-right cell
        if x == m - 1 and y == n - 1:
            return 1 if xor_value == k else 0

        # Check memoization table
        if (x, y, xor_value) in dp:
            return dp[(x, y, xor_value)]

        paths = 0
        # Move right
        if y + 1 < n:
            paths += dfs(x, y + 1, xor_value ^ grid[x][y + 1])
        # Move down
        if x + 1 < m:
            paths += dfs(x + 1, y, xor_value ^ grid[x + 1][y])

        # Store the result in the memoization table
        dp[(x, y, xor_value)] = paths % MOD
        return dp[(x, y, xor_value)]

    # Start DFS from (0, 0) with the initial XOR value as the grid's top-left cell
    return dfs(0, 0, grid[0][0])
    
if __name__ == "__main__":
    grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]]
    k = 11
    print("Count Paths with given XOR: ", countPathsWithXORValue(grid, k))
