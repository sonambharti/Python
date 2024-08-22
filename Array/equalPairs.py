'''
# 2352. Equal row and column pair

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the 
same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

'''
from collections import defaultdict
def equalPairs(grid):
    gridset = defaultdict(int)
    rotatedgrid = list(zip(*grid))
    ans = 0
    for row in grid :
        gridset[tuple(row)] += 1
    for column in rotatedgrid :
        if column in gridset :
            ans += gridset[tuple(column)]
    return ans

        
if __name__ == "__main__":
    grid = [[3,2,1],[2,7,6],[1,7,7]]
    res = equalPairs(grid)
    
    print("No. of equal Row-Col Pairs in matrix: ", res)
