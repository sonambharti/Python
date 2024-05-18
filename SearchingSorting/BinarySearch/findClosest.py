"""
Given a sorted array arr[] of positive integers. The task is to find the closest value in the 
array to the given number k. The array may contain duplicate values.

Note: If the difference with k is the same for two values in the array return the greater value.

Example 1:

Input: 
n = 4
k = 4
arr[] = {1, 3, 6, 7}
Output: 
3
Explanation:
We have array arr={1, 3, 6, 7} and target is 4. If we look at the absolute difference of target 
with every element of the array we will get { |1-4|, |3-4|, |6-4|, |7-4| }  = {3, 1, 2, 3}. So, 
the closest number is 3.
"""

import math, sys
def findClosest(n, k, arr):
    # code here
    start = 0
    end = n-1
    minm = sys.maxsize
    ans = 0
    while start <= end:
        mid = start + (end-start)//2
        diff = abs(k-arr[mid])
        if(diff <= minm and (diff < minm or arr[mid] > ans)):
            ans = arr[mid]
            minm = diff
        if arr[mid] == k:
            return ans
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans
    
if __name__ == "__main__":
    n = 7
    k = 4
    arr = [1, 2, 3, 5, 6, 8, 9]
    print(f"The closest element of k = {k} in the given array is: ", findClosest(n, k, arr))
