"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    Example: 
    1 2 3          3 2 1                7 4 1
    4 5 6   ->     6 5 4       ->       8 5 2
    7 8 9          9 8 7                9 6 3
    """
    rev_matrix = []
    for rows in matrix:
      rows.reverse()
      rev_matrix.append(rows)
    
    n = len(matrix)
    for rows in range(n):
      for cols in range(n-rows):
        rev_matrix[rows][cols], rev_matrix[n-cols-1][n-rows-1] = rev_matrix[n-cols-1][n-rows-1], rev_matrix[rows][cols]

    return rev_matrix
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = rotate(matrix)
print("Matrix after rotation:\n", res)
