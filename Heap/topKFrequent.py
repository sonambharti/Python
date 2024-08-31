'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
'''


import heapq
from collections import Counter

def topKFrequent(nums, k):
    freq_dict = {}
    # Step 1: Count frequencies of elements in nums
    for element in nums:
        # Get the current frequency of the element, default to 0 if it's not present
        freq_dict[element] = freq_dict.get(element, 0) + 1
    # freq_dict = Counter(nums) # Sort using Counter
    
    # Step 2: Build a min-heap of size k based on frequency
    min_heap = []
    
    for num, freq in freq_dict.items():
        heapq.heappush(min_heap, (freq, num))
        
        # If the heap grows larger than k, remove the smallest element (to keep only top k elements)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Step 3: Extract the k most frequent elements from the heap
    top_k_frequent = [item[1] for item in min_heap]
    
    return top_k_frequent

# Example usage:
if __name__ == "__main__":
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print("The k most frequent elements are: ", topKFrequent(nums1, k1))  # Output: [1, 2]
    
    nums2 = [1]
    k2 = 1
    print("The k most frequent elements are: ", topKFrequent(nums2, k2))  # Output: [1]
