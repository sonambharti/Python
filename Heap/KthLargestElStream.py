"""
# 215. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the 
kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the 
stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element 
representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

"""

import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # Convert nums into a heap
        # If the heap is larger than k, remove the smallest elements until it has exactly k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        # If after adding the new value, the heap has more than k elements, pop the smallest
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # The smallest element in the heap is now the k-th largest element
        return self.nums[0]
        


if __name__ == '__main__':
    # 	n = int(input())
    # 	nums = list(map(int, input().split()))
    # 	k = int(input())
	k = 3
	nums = [4, 5, 8, 2]
	obj = KthLargest(k, nums)
	param_1 = obj.add(3)
# 	param_1 = obj.add(5)
	print(param_1)
