"""
Given an array arr of size n containing non-negative integers, 
the task is to divide it into two sets S1 and S2 such that the 
absolute difference between their sums is minimum and find the 
minimum difference


Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5} 
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11  
"""
import sys, math
def minDifferenceSubset(arr, n):
    def isSubsetSum(arr, n, Range):
    # Initialize the dp array
        dp = [[False] * (Range + 1) for _ in range(n + 1)]
    
        # If sum is 0, then answer is True (empty subset)
        for i in range(n + 1):
            dp[i][0] = True
    
        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(1, Range + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        # print(dp[n])
    
        # Return the value in the bottom-right corner of the dp array
        return dp[n]
    sume = 0
    for i in arr:
        sume += i
        
    resArr = isSubsetSum(arr, n, sume)
    m = len(resArr)
    vec = []
    for i in range(math.ceil(m/2)):
        if resArr[i]==True:
            vec.append(i)
    
    minm = sys.maxsize
    for i in range(len(vec)):
        minm = min(minm, sume-2*vec[i])
        
    return minm
    
   
        
if __name__ == "__main__":
  # Example usage
  arr = [1, 6, 11, 5]
  n = len(arr)
  print(minDifferenceSubset(arr, n))

