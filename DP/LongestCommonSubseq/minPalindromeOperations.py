"""
# Minimum number of deletions.
Given a string 'str' of size ‘n’. The task is to remove or delete the minimum number of 
characters from the string so that the resultant string is a palindrome. Find the minimum 
number of characters we need to remove.
Note: The order of characters should be maintained.

Example 1:

Input: n = 7, str = "aebcbda"
Output: 2
Explanation: We'll remove 'e' and
'd' and the string become "abcba".

# Minimum number of Insertions.
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd

# minim No of Insertions = minm No of Deletions

"""


def minPalindromeOperations(Str):
	# code here
	n = len(Str)
	rev_Str = Str[::-1]
	dp = [[0]*(n+1) for _ in range(n+1)]
	
	for i in range(1, n+1):
	    for j in range(1, n+1):
	        if (i==0 or j==0):
	            dp[i][j] = 0
	        elif Str[i-1] == rev_Str[j-1]:
	            dp[i][j] = 1 + dp[i-1][j-1]
	        else:
	            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	            
#  	noOfDel = n - dp[n][n]
	noOfInsertion = n - dp[n][n]

	return noOfInsertion
    
    
if __name__ == "__main__":
    Str = "abcd"
    res = minPalindromeOperations(Str)
    print("Minimum no of insertion to make it palindrome: ", res)
