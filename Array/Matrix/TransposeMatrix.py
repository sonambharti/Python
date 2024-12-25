# Transpose Matrix

def transpose(A,B): 
    N = len(A[0])
    M = len(A)
    for i in range(N): 
        for j in range(M): 
            B[i][j] = A[j][i] 
    print(B)

def transposeInPlace(mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n): 
        for j in range(i): 
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    return mat
    
if __name__ == "__main__":
    # take a 3x4 matrix    
    A = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
    # B = A[:][:]
    B = [[0]*len(A) for _ in range(len(A[0]))]
    
    transpose(A,B)
    print(transposeInPlace(A))
   
    
