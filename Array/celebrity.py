'''
# The celebrity problem

A celebrity is a person who is known to all but does not know anyone at a party. A party 
is being organized by some people.  A square matrix mat is used to represent people at 
the party such that if an element of row i and column j is set to 1 it means ith person 
knows jth person. You need to return the index of the celebrity in the party, if the 
celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[0 1 0],
                [0 0 0], 
                [0 1 0]]
Output: 1
Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity. 
Input: mat[][] = [[0 1],
                [1 0]]
Output: -1
Explanation: The two people at the party both know each other. None of them is a celebrity.

'''
def celebrity(mat):
    # code here
    n = len(mat)
    knowMe = [0]*n
    Iknow = [0]*n
    
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                knowMe[j] += 1 # ith person knows jth person
                Iknow[i] += 1 
    
    for i in range(n):
        if knowMe[i] == n - 1 and Iknow[i] == 0:
                return i 

    return -1

if __name__ == "__main__":
    mat = [[0, 1, 0],
            [0, 0, 0], 
            [0, 1, 0]]
    
    res = celebrity(mat)
    print("Index of the celebrity in the room is: ", res)
