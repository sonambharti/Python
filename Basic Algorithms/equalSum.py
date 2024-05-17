"""
Equal Sum -> GFG (medium Array)
Given an array Arr of length N. Determine if there exists an element in the array 
such that the sum of the elements on its left is equal to the sum of the elements 
on its right. If there are no elements to the left/right, then the sum is considered to be zero. 
Formally, find an i, such that, Arr1 + Arr2 ... Arri-1 = Arri+1 + Arri+2 ... ArrN.

Example 1:

Input:
N = 4
Arr[] = {1, 2, 3, 3}
Output: YES
Explanation: Consider i = 3, for [1, 2] sum is 3 and for [3] sum is also 3.
"""
def equilibrium(arr, n):
    prefsum = [0] * n
    prefsum[0] = arr[0]
    sumi = 0

    for i in arr:
        sumi += i
        
    for i in range(1, len(arr)):
        prefsum[i] = prefsum[i - 1] + arr[i]
    
    for i in range(n):
        if prefsum[i]-arr[i] == sumi - prefsum[i]:
            return "YES"
    return "NO"
    
if __name__ == "__main__":
  # Example usage
  arr = [3, 3, 4, 12, 2, 5]
  
  n = len(arr)
  print(equilibrium(arr, n))
