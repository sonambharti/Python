'''
# Set Matrix Zeroes

You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, 
all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity.

Examples:

Input: mat[][] = [[1, -1, 1],
                [-1, 0, 1],
                [1, -1, 1]]
Output: [[1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]]
Explanation: mat[1][1] = 0, so all elements in row 1 and column 1 are updated to zeroes.
Input: mat[][] = [[0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]]
Output: [[0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]]
Explanation: mat[0][0] and mat[0][3] are 0s, so all elements in row 0, column 0 and column 3 are updated to zeroes.
'''


def setMatrixZeroes(mat):
    n = len(mat)
    m = len(mat[0])
    
    rowZero = False
    colZero = False
    
    # Check if the first row needs to be zeroed      
    for j in range(m):
        if mat[0][j] == 0:
            rowZero = True
            break
       
    # Check if the first column needs to be zeroed 
    for i in range(n):
        if mat[i][0] == 0:
            colZero = True
            break
        
    # Mark rows and columns to be zeroed using the first row and column
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
                
                
    # Zero out cells based on the markers in the first row and column
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][0] == 0 or mat[0][j] == 0:
                mat[i][j] = 0
            
    
    # Zero out the first row if necessary
    if rowZero :
        for j in range(m):
            mat[0][j] = 0
            
    # Zero out the first col if necessary
    if colZero :
        for i in range(n):
            mat[i][0] = 0
            
    return mat
    
if __name__ == "__main__":
    mat = [[1, -1, 1],
            [-1, 0, 1],
            [1, -1, 1]]
            
    print(setMatrixZeroes(mat))
    
    
