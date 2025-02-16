'''
# Word Search

You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. 
Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells,
either horizontally or vertically. The same cell cannot be used more than once.

Examples :

Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: true

'''

    
    
def isWordExist(mat, word):
	#Code here
	n = len(mat)
	m = len(mat[0])
	
	def dfs(i, j, k):
	    if k == len(word):
	        return True
	        
	    if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[k]:
	        return False
	    temp = mat[i][j]
	    mat[i][j] = ''
	    if dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1):
	        return True
	    mat[i][j] = temp
	    return False
        
	for i in range(n):
	    for j in range(m):
	        if dfs(i, j, 0):
	            return True
	return False
    
	    
if __name__ == "__main__":
    mat = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
    word = "GEEK"
    print("Is this word available in the matrix: ", isWordExist(mat, word))
    
