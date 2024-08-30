'''
# n-Queen Problem
# 51. N-Queens

The n-queens puzzle is the problem of placing n queens on a (n×n) chessboard such 
that no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle. Each 
solution contains distinct board configurations of the n-queens placement, where 
the solutions are a permutation of [1,2,3..n] in increasing order, here the number 
in the ith place denotes that the ith-column queen is placed in the row with that 
number. For eg below figure represents a chessboard [3 1 4 2].



Examples:

Input: 1
Output: [1]
Explaination: Only one queen can be placed in the single cell available.
Input: 4
Output: [[2 4 1 3 ],[3 1 4 2 ]]
Explaination: These are the 2 possible solutions.
Expected Time Complexity: O(n!)
Expected Auxiliary Space: O(n2) 

Constraints:
1 ≤ n ≤ 10


'''

# Print all the locations in each row where Queen should be placed
def nQueenOptimized(n):
    mat = [0] * n
    def check(mat, indx):
        i = indx - 1
        while i > -1:
            if (mat[i] == mat[indx]) or (mat[indx] - mat[i] == indx - i) or (mat[indx] - mat[i] == i - indx): 
                return False
            i -= 1
        return True
        
    def rec(indx, mat, n):
        if indx == n:
            ans.append(mat.copy())
            return
        for i in range(n):
            mat[indx] = i+1
            if check(mat, indx):
                mat[indx] = i + 1
                rec(indx+1, mat, n)
    ans = []
    rec(0, mat, n)
    return ans
    
    
# Print the board where Queen is placed
def nQueen(n):
    # code here
    cols = set()
    posDiagonal = set() # (row + col)
    negDiagonal = set() # (row - col)
    
    res = []
    board = [['.'] * n for _ in range(n)]
    
    def backtrack(row):
        if row == n:
            # copy = ["".join(row) for row in board] # For Leetcode Problem
            copy = [list(row) for row in board]
            res.append(copy)
            return
        
        for col in range(n):
            if col in cols or (row + col) in posDiagonal or (row - col) in negDiagonal:
                continue
            
            cols.add(col)
            posDiagonal.add(row + col)
            negDiagonal.add(row - col)
            board[row][col] = 'Q'
            
            backtrack(row + 1)
            
            cols.remove(col)
            posDiagonal.remove(row + col)
            negDiagonal.remove(row - col)
            board[row][col] = '.'
        
        
    backtrack(0)
    ans = []
    temp = []
    for rows in res:
        # print(row)
        for row in rows:
            # print(i)
            for j in range(n):
                if row[j] == 'Q':
                    temp.append(j + 1)
        ans.append(temp)
        temp = []
    
    return ans
    # return res # For Leetcode Problem


if __name__=='__main__':
    
    n = 4
    print("Print all the locations in each row where Queen should be placed: ",nQueen(n))
    print("Print all the locations in each row where Queen should be placed: ", nQueenOptimized(1))
    
