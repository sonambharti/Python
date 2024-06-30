"""
# Minimum number of deletions and insertions
Given two strings str1 and str2. The task is to remove or insert the minimum number of 
characters from/in str1 so as to transform it into str2. It could be possible that the same 
character needs to be removed/deleted from one point of str1 and inserted to some another point.

Example 1:

Input: str1 = "heap", str2 = "pea"
Output: 3
Explanation: 2 deletions and 1 insertion.
p and h deleted from heap. Then, p is inserted at the beginning.
One thing to note, though p was required yet it was removed/deleted first from its position 
and then it is inserted to some other position. Thus, p contributes one to the 
deletion_count and one to the insertion_count.
"""

def minOperations(s1, s2):
	# code here
	n = len(s1)
	m = len(s2)
	dp = [[-1]*(m+1) for _ in range(n+1)]
	
	for i in range(n+1):
	    for j in range(m+1):
	        if (i==0 or j==0):
	            dp[i][j] = 0
	        elif s1[i-1] == s2[j-1]:
	            dp[i][j] = 1 + dp[i-1][j-1]
	        else:
	            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	            
	noOfDel = n - dp[n][m]
	noOfInsertion = m - dp[n][m]
	print("No of Deletion: ", noOfDel)
	print("No. of Insertion: ", noOfInsertion)
	return (noOfDel+noOfInsertion)
    
    
if __name__ == "__main__":
    str1 = "abchiyp"
    str2 = "abpu"
    n = len(str1)
    m = len(str2)
  
    res = minOperations(str1, str2)
    print(res)
