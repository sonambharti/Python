

def transpose(A,B): 
    N = len(A[0])
    M = len(A)
    for i in range(N): 
        for j in range(M): 
            B[i][j] = A[j][i] 
    print(B)
   
if __name__ == "__main__":
    # take a 3x4 matrix    
    A = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
    # B = A[:][:]
    B = [[0]*len(A) for _ in range(len(A[0]))]
    
    transpose(A,B)
   
    
