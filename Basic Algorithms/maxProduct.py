'''
# Maximum Product Subarray

Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr.

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is {-3, -10} with product = (-3) * (-10) = 30.
'''

import sys

def maxProduct_bruteforce(arr):
	# code here
	prod_res = -sys.maxsize
	n = len(arr)
	
	for i in range(n):
	    mul = 1
	    for j in range(i, n):
		    mul *= arr[j]
		    if arr[j]==0:
		        prod_res = max(prod_res, arr[j])
		        break
		    prod_res = max(prod_res, mul)
	return prod_res
	
	
def maxProduct(arr):
    n = len(arr)
    prod_res = max(arr)
    currMax, currMin = 1, 1
    
    for i in range(n):
        if arr[i] < 0:
            currMax, currMin = currMin, currMax
        currMax = max(arr[i]*currMax, arr[i])
        currMin = min(arr[i]*currMin, arr[i])
        prod_res = max(prod_res, currMax)
    
    return prod_res
    
    
if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print("Maxm Product in Brute Force approach:", maxProduct_bruteforce(arr))
    print("Maxm Product: ", maxProduct(arr))
