"""
# Kth Smallest Element in an Array

Given an array arr[] and an integer k where k is smaller than the size of the array, 
the task is to find the kth smallest element in the given array. It is given that all 
array elements are distinct.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.
Input: arr[] = [7, 10, 4, 20, 15], k = 4 
Output:  15
Explanation: 4th smallest element in the given array is 15.
 
"""

from collections import deque
from heapq import *

def kthSmallest(n, arr,k):
    
    # For using min-heap as max-heap, multiply array element with (* -1)
    for i in range(n):
        arr[i] = -1 * arr[i]
    
    heap = arr[:k]
    heapify(heap)
    
    # Approaching kthSmallest element using min-heap with multiplied by -1
    for j in range(k, n):
        if arr[j] > heap[0]:
            heapreplace(heap, arr[j])
            
    # Converting min-heap to max-heap using (* -1).
    for i in range(k):
        heap[i] = -1 * heap[i]
    
    # returning kthSmallest element in array
    return heap[0]
        
        
        
if __name__ == '__main__':
	nums = [7, 10, 4, 3, 20, 15]
	k = 3
	n = len(nums)
	result = kthSmallest(n, nums, k)
	print(f" {k}th smallest no in the given array is: ", result)
