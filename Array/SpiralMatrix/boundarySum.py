"""
# Boundary Sum of a matrix

You are given an integer matroix of size n X n. You have to find the sum 
of each level boundary in the matrix.
For more details see below examples -

Example 1:
    Input:
    n = 4
    matrix = 
        [    
          [ 1 2 3 4 ],
          [ 2 3 4 5 ],  
          [ 4 1 5 2 ],
          [ 3 2 9 0 ]
        ]
    
    Output: [37, 13]
    
    Explanation: 
    First Boundary Sum = (1+2+3+4+5+2+0+9+2+3+4+2) = 37
    Second Boundary Sum = (3+4+5+1) = 13
    
"""


def boundarySum(n, arr):
    # code here
    """
            l   r
        t [ 1 2 3 ],
          [ 4 5 6 ],  = [(1+2+3+6+9+8+7+4),5] = [40, 5]
        b [ 7 8 9 ]

    
    """
    res = []
    l, t = 0, 0
    r, b = n, n
    
    
    while l < r and t < b:
        summ = 0
        for i in range(l, r):
            summ += arr[t][i]
        t += 1
        
        for i in range(t, b):
            summ += arr[i][r-1]
        r -= 1
        
        for i in range(r-1, l-1, -1):
            summ += arr[b-1][i]
        b -= 1

        for i in range(b-1, t-1, -1):
            summ += arr[i][l]
        l += 1  
        res.append(summ)
    return res


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    n = len(matrix)
    res = boundarySum(n, matrix)
    print("Boundary Sum = ", res)
    
    
