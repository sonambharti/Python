'''

A farmer wants to farm their land with the maximum area
where good land is present, The "land" is represented 
as a matrix with 1s and 0s, where 1s mean good land and
0s mean bad land. The farmer only want to farm in a 
square of good land with the maximum ares. Please help
the farmer to find the maximum area of the land they 
can farm in good land.

Example:

0 1 1 0 1
1 2 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0

'''

def maximalSquare_BruteForce(matrix):
    # Time Complexity = O(R*C*k^3)
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    max_side = 0

    for r in range(rows):
        for c in range(cols):

            # Try every possible square size
            max_possible = min(rows - r, cols - c)

            for side in range(1, max_possible + 1):

                valid = True

                # Check every cell inside the square
                for i in range(r, r + side):
                    for j in range(c, c + side):
                        if matrix[i][j] != 1:
                            valid = False
                            break

                    if not valid:
                        break

                if valid:
                    max_side = max(max_side, side)

    return max_side * max_side
    
        
def maximalSquare_recursive(matrix):
    # Time Complexity = O(9^n)
    if not matrix or not matrix[0]:
        return 0
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    def solve_rec(r, c):
        if r < 0 or c < 0:
            return 0
        
        if matrix[r][c] == 0:
            return 0

        return 1 + min(solve_rec(r-1, c), solve_rec(r, c-1), solve_rec(r-1, c-1))
        
    
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            max_side = max(max_side, solve_rec(i, j))
            
    return max_side*max_side
    

def maximalSquare_memo(matrix):
    # Time Complexity = O(9^n)
    if not matrix or not matrix[0]:
        return 0
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    memo = {}
    
    def solve_rec(r, c):
        if r < 0 or c < 0:
            return 0
        
        if matrix[r][c] == 0:
            return 0
        
        if (r,c) in memo:
            return memo[(r,c)]
            
        memo[(r, c)] = 1 + min(solve_rec(r-1, c), solve_rec(r, c-1), solve_rec(r-1, c-1))
        
        return memo[(r, c)]
        
    
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            max_side = max(max_side, solve_rec(i, j))
            
    return max_side*max_side
    
    
def maximalSquare_dp_2D(matrix):
    # Time Complexity = O(R*C) = O(n^2)
    # Space Complexity = O(R*C) = O(n^2)
    if not matrix or not matrix[0]:
        return 0
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    dp = [[0]*(cols+1) for _ in range(rows+1)]
    
    max_side = 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r-1][c-1] == 1:
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
            max_side = max(max_side, dp[r][c])
        
    return max_side*max_side
    
    

def maximalSquare_dp_1D(matrix):
    # Time Complexity = O(R*C) = O(n^2)
    # Space Complexity = O(C) = O(n)
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    dp = [0] * (cols + 1)

    max_side = 0
    diagonal = 0

    for r in range(1, rows + 1):
        diagonal = 0

        for c in range(1, cols + 1):

            top = dp[c]

            if matrix[r - 1][c - 1] == 1:
                dp[c] = 1 + min(
                    dp[c],       # top
                    dp[c - 1],   # left
                    diagonal     # top-left diagonal
                )

                max_side = max(max_side, dp[c])
            else:
                dp[c] = 0

            diagonal = top

    return max_side * max_side
        

if __name__ == "__main__":
    matrix = [
            [0, 1, 1, 0, 1],
            [1, 2, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        
    res = maximalSquare_BruteForce(matrix)
    print(f"Brute Force = {res}")
    
    res1 = maximalSquare_recursive(matrix)
    print(f"recursion = {res1}")
    
    res2 = maximalSquare_memo(matrix)
    print(f"memoization = {res2}")
    
    res3 = maximalSquare_dp_2D(matrix)
    print(f"2D-DP = {res3}")
    
    res4 = maximalSquare_dp_1D(matrix)
    print(f"1D-DP = {res4}")
