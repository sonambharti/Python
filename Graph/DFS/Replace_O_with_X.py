"""
# Replace O's with X's
Given a matrix mat of size N x M where every element is either 'O' or 'X'. 
Replace all 'O' or a group of 'O' with 'X' that are surrounded by 'X'.

A 'O' (or a set of 'O') is considered to be surrounded by 'X' if there are 
'X' at locations just below, just above, just left and just right of it.

Example 1:

Input: 
n = 5, m = 4
mat = {{'X', 'X', 'X', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'O', 'O', 'X'}, 
       {'X', 'O', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
Output: 
ans = {{'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'X', 'X'}, 
       {'X', 'X', 'O', 'O'}}
"""
def fill(n, m, mat):
    # code here
    res = mat
    vis =[[False]*m for _ in range(n)]
    
    def dfs(res, sr, sc):
        lrow = [-1, 0, 1, 0]
        lcol = [0, -1, 0, 1]
        vis[sr][sc] = True
        for i in range(4): 
            curr_row = sr+lrow[i]
            curr_col = sc+lcol[i]
            if (0<=curr_row<n) and (0<=curr_col<m)and mat[curr_row][curr_col]=='O' and vis[curr_row][curr_col] == False:
                dfs(res, curr_row, curr_col)
    
    for i in range(n):
        if mat[i][0]=='O' and vis[i][0]==False:
            dfs(res, i, 0)
        if mat[i][m-1]=='O' and vis[i][m-1]==False:
            dfs(res, i, m-1)
            
    for j in range(m):
        if mat[0][j]=='O' and vis[0][j]==False:
            dfs(res, 0, j)
        if mat[n-1][j]=='O' and vis[n-1][j]==False:
            dfs(res, n-1, j)
            
    for i in range(n):
        for j in range(m):
            if vis[i][j]==False:
                res[i][j] = 'X'
            
    return res

if __name__ == "__main__":
    n=5
    m=4
    mat = [['X', 'X', 'X', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'O', 'O', 'X'], 
       ['X', 'O', 'X', 'X'], 
       ['X', 'X', 'O', 'O']]
    res = fill(n, m, mat)
    print("New matrix: \n", res)
