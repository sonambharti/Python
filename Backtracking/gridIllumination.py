"""
# 1001. Grid Illumination

There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp 
at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine 
whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at 
grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side
or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 
if the lamp was not.

 

Example 1:


Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: We have the initial grid with all lamps turned off. In the above picture we see the grid after
turning on the lamp at grid[0][0] then turning on the lamp at grid[4][4].
The 0th query asks if the lamp at grid[1][1] is illuminated or not (the blue square). It is illuminated, 
so set ans[0] = 1. Then, we turn off all lamps in the red square.

The 1st query asks if the lamp at grid[1][0] is illuminated or not (the blue square). It is not illuminated,
so set ans[1] = 0. Then, we turn off all lamps in the red rectangle.
"""

from collections import defaultdict, Counter

def gridIllumination_bactracking(n, lamps, queries):
    # Counters to track how many lamps are illuminating a particular row, column, or diagonal
    row_count = Counter()
    col_count = Counter()
    pos_diag_count = Counter()
    neg_diag_count = Counter()

    # Set to track the positions of the active lamps
    lamp_set = set()

    # Initialize the lamp sets and illumination counters
    for r, c in lamps:
        if (r, c) in lamp_set:
            continue
        lamp_set.add((r, c))
        row_count[r] += 1
        col_count[c] += 1
        pos_diag_count[r + c] += 1
        neg_diag_count[r - c] += 1

    # Directions to turn off adjacent lamps (including the lamp itself)
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    result = []

    def is_illuminated(r, c):
        # Check if the current cell is illuminated by any lamp in the same row, column, or diagonals
        return row_count[r] > 0 or col_count[c] > 0 or pos_diag_count[r + c] > 0 or neg_diag_count[r - c] > 0

    def turn_off_lamps(r, c):
        # Turn off the lamp at (r, c) and its adjacent cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in lamp_set:
                lamp_set.remove((nr, nc))
                # Update illumination counters
                row_count[nr] -= 1
                col_count[nc] -= 1
                pos_diag_count[nr + nc] -= 1
                neg_diag_count[nr - nc] -= 1

    # Process each query
    for r, c in queries:
        if is_illuminated(r, c):
            result.append(1)  # The cell is illuminated
        else:
            result.append(0)  # The cell is not illuminated

        # Turn off the lamp at (r, c) and its adjacent cells
        turn_off_lamps(r, c)

    return result


# Optimal Solution using hash maps 
def gridIllumination_optimal(n, lamps, queries):
    # Maps to store the number of lamps in each row, column, and diagonal
    row_map = defaultdict(int)
    col_map = defaultdict(int)
    pos_diag_map = defaultdict(int)
    neg_diag_map = defaultdict(int)
    
    # Set to track the positions of the active lamps
    lamp_set = set()

    # Initialize the lamp maps and lamp set
    for r, c in lamps:
        if (r, c) in lamp_set:
            continue
        lamp_set.add((r, c))
        row_map[r] += 1
        col_map[c] += 1
        pos_diag_map[r + c] += 1
        neg_diag_map[r - c] += 1
    
    # Directions to turn off adjacent lamps (including the lamp itself)
    directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    result = []

    for r, c in queries:
        # Check if the current cell is illuminated
        if row_map[r] > 0 or col_map[c] > 0 or pos_diag_map[r + c] > 0 or neg_diag_map[r - c] > 0:
            result.append(1)  # The cell is illuminated
        else:
            result.append(0)  # The cell is not illuminated

        # Turn off the lamp at (r, c) and its adjacent cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in lamp_set:
                lamp_set.remove((nr, nc))
                row_map[nr] -= 1
                col_map[nc] -= 1
                pos_diag_map[nr + nc] -= 1
                neg_diag_map[nr - nc] -= 1

    return result

    
# Example usage:
if __name__ == "__main__":
    n = 5
    lamps = [[0,0],[4,4]]
    queries = [[1,1],[1,1]]
    print(gridIllumination_bactracking(n, lamps, queries))  # Output: [1,1]
    print(gridIllumination_optimal(n, lamps, queries))
