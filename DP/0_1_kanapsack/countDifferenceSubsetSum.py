"""
Given an array arr of size n containing non-negative integers, 
the task is to divide it into two sets S1 and S2 such that the 
absolute difference between their sums is minimum and find the 
count of the Subset sum difference


Example 1:

Input: Arr = [1,1,2,3] ; diff= 1
Output: 3 
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1, s1 = 12 
Subset2 = {11}, sum of Subset2, s2 = 11  


Note: Mathematics logic
s1 and s2 are the sums of 2 subsets of the given array. So,
s1 + s2 = s (Total sum of the array). -------> (eqn i)
and, we have s1 - s2 = diff. --------> (eqn ii)
Now, By adding (eqn i) and (eqn ii), we have:
2*s1 = s + diff
=> s1 = (s + diff)/2

"""
import sys, math
def countDifferenceSubsetSum(arr, n, diff):
    def isSubsetSum(arr, n, sumn):
    # Initialize the dp array
        dp = [[0] * (sumn + 1) for _ in range(n + 1)]
    
        # If sum is 0, then answer is True (empty subset)
        for i in range(n + 1):
            dp[i][0] = 1
    
        # Fill the dp array
        for i in range(1, n + 1):
            for j in range(1, sumn + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - arr[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
    
        # Return the value in the bottom-right corner of the dp array
        return dp[n][sumn]
    sume = 0
    for i in arr:
        sume += i
        
    s1 = (sume+diff)//2
        
    countDiff = isSubsetSum(arr, n, s1)
        
    return countDiff
    
   
        
if __name__ == "__main__":
  # Example usage
  arr = [1, 2, 3, 1, 2]
  n = len(arr)
  diff = 1
  print(countDifferenceSubsetSum(arr, n, diff))
