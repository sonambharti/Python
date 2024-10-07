"""
# Largest Pair Sum

Find the largest pair sum in an array of distinct integers.

Examples :

Input: arr[] = [12, 34, 10, 6, 40]
Output: 74
Explanation: Sum of 34 and 40 is the largest, i.e, 34 + 40 = 74.
Input: arr[] = [10, 20, 30]
Output: 50
Explanation: 20 + 30 = 50.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
"""

from heapq import nlargest
def pairsum(arr):
      # code here
      return sum(nlargest(2, arr))

if __name__ == "__main__":
  arr = [12, 34, 10, 6, 40]
  print("Largest pair sum of given array is: ", pairsum(arr))

      
