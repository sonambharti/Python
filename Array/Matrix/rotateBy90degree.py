'''
# Rotate By 90 degree

Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in
an anti-clockwise direction without using any extra space. 

Examples:

Input: mat[][] = [[1, 2, 3],
                [4, 5, 6]
                [7, 8, 9]]
Output: Rotated Matrix:
[3, 6, 9]
[2, 5, 8]
[1, 4, 7]
Input: mat[][] = [[1, 2],
                [3, 4]]
Output: Rotated Matrix:
[2, 4]
[1, 3]
'''


def rotateby90(mat): 
    # code here
    n = len(mat)
    m = len(mat[0])
    
    for i in range(n):
        mat[i] = mat[i][::-1]
        
    for i in range(n): 
        for j in range(i): 
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    return mat
            
    
if __name__ == "__main__":
    mat = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
            
    print(rotateby90(mat))
    
    
