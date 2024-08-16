"""
# 215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
"""

from collections import deque
from heapq import *

def findKthLargest(n, nums, k):
    # CODE HERE
    heap = nums[:k]
    heapify(heap)

    for i in range(k,n):
        if nums[i] > heap[0]:
            heapreplace(heap, nums[i])
    
    return heap[0]

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	k = int(input())
	result = findKthLargest(n, nums, k)
	print(result)
