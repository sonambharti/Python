"""
# 59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]

"""
def generateMatrix(n):
    res_mat = [[-1] * n for _ in range(n)]

    l = 0
    r = n
    t = 0
    b = n
    el = 1

    while l < r and t < b:
        for i in range(l, r):
            res_mat[t][i] = el
            el += 1
        t += 1

        for i in range(t, b):
            res_mat[i][r-1] = el
            el += 1
        r -= 1

        if not (l < r and t < b):
            break

        for i in range(r-1, l-1, -1):
            res_mat[b-1][i] = el
            el += 1
        b -= 1

        for i in range(b-1, t-1, -1):
            res_mat[i][l] = el
            el += 1
        l += 1
    
    return res_mat
    
if __name__ == "__main__":
    n = 3
    res = generateMatrix(n)
    print("Print the resultant matrix: ", res)
    
