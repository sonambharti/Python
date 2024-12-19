import numpy as np 

def matrixMultiplication(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    result = np.dot(A,B)
    return result
    
    
def matrixMultiplication_BruteForce(A, B):
    # result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    result = [[0]*len(B[0]) for _ in range(len(A))]
    
    # iterating by row of A
    for i in range(len(A)):
        # iterating by column by B 
        for j in range(len(B[0])):
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    # for r in result:
    #     print(r)  
        
    return result


if __name__ == "__main__":
    # take a 3x3 matrix
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]
    
    # take a 3x4 matrix    
    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
    
    print("Brute Force Matrix Multiplication:\n", matrixMultiplication_BruteForce(A,B))
    res = matrixMultiplication(A, B)
    print(res)
    
