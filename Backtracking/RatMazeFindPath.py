'''
# Rat in a maze problem

Consider a rat placed at (0, 0) in a square matrix mat of order n* n. It has to 
reach the destination at (n - 1, n - 1). Find all possible paths that the rat 
can take to reach from source to destination. The directions in which the rat 
can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in 
the matrix represents that it is blocked and rat cannot move to it while value 
1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell 
is 0, the rat cannot move to any other cell. In case of no path, return an 
empty list. The driver will output "-1" automatically.

Examples:

Input: mat[][] = [[1, 0, 0, 0],
                [1, 1, 0, 1], 
                [1, 1, 0, 0],
                [0, 1, 1, 1]]
Output: DDRDRR DRDDRR
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two 
paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.

'''


def hasPath(inputM, n, visited, x, y):
    if (x == n-1 and y == n-1):
        return True
                
    if (x < 0 or y < 0 or x >= n or y >=n or inputM[x][y] == 0 or visited[x][y] == 1):
        return False
    
    visited[x][y] = 1
    if hasPath(inputM, n, visited, x+1, y):
        return True
    if hasPath(inputM, n, visited, x, y-1):
        return True
    if hasPath(inputM, n, visited, x-1, y):
        return True
    if hasPath(inputM, n, visited, x, y+1):
        return True
    visited[x][y] = 0
    
    return False
    
    

def printPath(inputM, n, visited, x, y, res, move):
    if (x==n-1 and y==n-1):
        res.append(move)
        return
    
    if (x+1 < n and inputM[x+1][y] == 1 and not visited[x+1][y]):
        visited[x][y] = 1
        printPath(inputM, n, visited, x+1, y, res, move + 'D')
        visited[x][y] = 0
        
    if (y-1 >= 0 and inputM[x][y-1] == 1 and not visited[x][y-1]):
        visited[x][y] = 1
        printPath(inputM, n, visited, x, y-1, res, move + 'L')
        visited[x][y] = 0
        
    if (x-1 >= 0 and inputM[x-1][y] == 1 and not visited[x-1][y]):
        visited[x][y] = 1
        printPath(inputM, n, visited, x-1, y, res, move + 'U')
        visited[x][y] = 0
        
    if (y+1 < n and inputM[x][y+1] == 1 and not visited[x][y+1]):
        visited[x][y] = 1
        printPath(inputM, n, visited, x, y+1, res, move + 'R')
        visited[x][y] = 0
    
        
def findPath(m):
    # code here
    n = len(m)
    visited = [[0] * n for _ in range(n)]
    res = []
    x, y = 0, 0
    if m[0][0] == 1:
        printPath(m, n, visited, x, y, res, '')
    return res
    
    
    
    
def helper(i, j, a, n, ans, move, vis, di, dj):
    if i == n - 1 and j == n - 1:
        ans.append(move)
        return
    dir = "DLRU"
    for ind in range(4):
        nexti = i + di[ind]
        nextj = j + dj[ind]
        if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1:
            vis[i][j] = 1
            helper(nexti, nextj, a, n, ans,
                       move + dir[ind], vis, di, dj)
            vis[i][j] = 0
            
            
def optimized_FindPath(m):
    n = len(m)
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    di = [+1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    if m[0][0] == 1:
        helper(0, 0, m, n, ans, "", vis, di, dj)
    return ans



if __name__=='__main__':
    
    # mat = [[1, 0],
    #       [1, 0]]
    mat= [[1, 0, 0, 0],
          [1, 1, 0, 1], 
          [1, 1, 0, 0],
          [0, 1, 1, 1]]
          
    n = len(mat)
    visited = [[0] * n for _ in range(n)]
    x, y = 0, 0
    if mat[0][0] == 1:
        print("Is there a path to exit: ", hasPath(mat, n, visited, x, y))
    print("Print all the possible path to exit the maze: ",findPath(mat))
    # print("Print all the possible path to exit the maze: ",optimized_FindPath(mat))
    
