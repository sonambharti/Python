"""
Given an N x N grid, where each cell contains a direction (U, D, L, R), 
determine if you can reach (N, N) from (0,0).
"""
def can_reach_end(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    def dfs(x, y):
        if not is_valid(x, y) or visited[x][y]:
            return False
        if (x, y) == (n - 1, n - 1):
            return True
        visited[x][y] = True

        direction = grid[x][y]
        if direction == 'U':
            return dfs(x - 1, y)
        elif direction == 'D':
            return dfs(x + 1, y)
        elif direction == 'L':
            return dfs(x, y - 1)
        elif direction == 'R':
            return dfs(x, y + 1)
        return False

    return dfs(0, 0)


# Example usage:
grid = [
    ['R', 'D', 'L'],
    ['U', 'D', 'D'],
    ['L', 'U', 'D']
]
# grid = [
#     ['R', 'D', 'L'],
#     ['U', 'D', 'D'],
#     ['L', 'R', 'D']
# ]

print(can_reach_end(grid))  # Output: True or False depending on grid
