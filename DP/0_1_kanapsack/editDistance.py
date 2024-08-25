'''
# Edit Distance

Given two strings str1 and str2. Return the minimum number of operations required to convert str1 to str2.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.
Examples:

Input: str1 = "geek", srt2 = "gesek"
Output: 1
Explanation: One operation is required, inserting 's' between two 'e'.
Input : str1 = "gfg", str2 = "gfg"
Output: 0
Explanation: Both strings are same.

'''


def editDistance(s1, s2):
	# Code here
	n = len(s1)
	m = len(s2)
	dp = [[-1]*(m+1) for _ in range(n+1)]
	
	for i in range(n+1):
	    for j in range(m+1):
	        if i==0:
	            dp[i][j] = j
	        if j==0:
	            dp[i][j] = i
	        if dp[i][j] != -1:
	            dp[i][j] = dp[i][j]
	        elif s1[i-1] == s2[j-1]:
	            dp[i][j] = dp[i-1][j-1]
	        else:
	            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
	            

	return dp[n][m]
	
	
if __name__ == "__main__":
    str1 = "geek"
    srt2 = "geseos"
    
    res = editDistance(str1, srt2)
    
    print("The minimum number of operations required to convert str1 to str2: ", res)
