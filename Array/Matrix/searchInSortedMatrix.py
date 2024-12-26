'''
# Search in a sorted Matrix

Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number 
x is present in the matrix or not.

Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the 
first element of the ith row (i!=0) is greater than the last element of the (i-1)th row.

Examples:

Input: mat[][] = [[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14
Output: true
Explanation: 14 is present in the matrix, so output is true.

Input: mat[][] = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42
Output: false
Explanation: 42 is not present in the matrix.

Input: mat[][] = [[87, 96, 99], [101, 103, 111]], x = 101
Output: true
Explanation: 101 is present in the matrix.
'''

def searchMatrix_brutForce(mat, x): 
	# code here 
	n = len(mat)
	m = len(mat[0])
	for i in range(n):
	    for j in range(m):
	        if mat[i][j] == x:
	            return True
	return False


# Search in sorted matrix using Binary Search
def searchMatrix(mat, x): 
    # code here 
	n = len(mat)
	m = len(mat[0])
	
	left, right = 0, n * m - 1
	
	while left <= right:
	    mid = (left + right) // 2
	    row, col = divmod(mid, m)  # Map 1D index to 2D matrix coordinates
	    mid_value = mat[row][col]
	    
	    if mid_value == x:
	        return True
	    elif mid_value < x:
	        left = mid + 1
	    else:
	        right = mid - 1
	        
	return False

            
    
if __name__ == "__main__":
    mat = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
            
    print("Search in matrix in Brute Force: ", searchMatrix_brutForce(mat, 8))
    
    print("Search in matrix using Binary Search: ", searchMatrix(mat, 12))
    
    
