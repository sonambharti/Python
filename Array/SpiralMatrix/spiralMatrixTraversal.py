"""
# 54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""

def spiralOrder(matrix):

    """
            l   r
        t [ 1 2 3 ],
          [ 4 5 6 ],        
        b [ 7 8 9 ]

        direction -> d
        # 1 2 3     -> row d = 0
        # 6 9       -> col d = 1
        # 8 7       -> row d = 2
        # 4         -> col d = 3
    """

    res = []
    rows = len(matrix)
    cols = len(matrix[0]) 

    if rows == 0:
        return res

    l = 0
    r = cols-1
    t = 0
    b = rows-1
    d = 0

    while (l <= r and t <= b):
      if d == 0:
        for i in range(l, r+1, 1):
            res.append(matrix[t][i])
        d = 1
        t += 1

      elif d == 1:
        for i in range(t, b+1, 1):
            res.append(matrix[i][r])
        d = 2
        r -= 1

      elif d == 2:
        for i in range(r, l-1, -1):
          res.append(matrix[b][i])
        d = 3
        b -= 1

      elif d==3:
        for i in range(b, t-1, -1):
          res.append(matrix[i][l])
        d = 0
        l += 1
    
    return res
            
        
        
    
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = spiralOrder(matrix)
print("Spiral Order Matrix Traversal:", res)
