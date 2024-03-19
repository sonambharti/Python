'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''
    
def subarray_sum_sliding_window(nums, k):
    count = 0
    sum_freq = {0: 1}  # Initialize with 0 to handle cases where cumulative sum equals k
    window_sum = 0
    
    for num in nums:
        window_sum += num
        complement = window_sum - k
        
        if complement in sum_freq:
            count += sum_freq[complement]
        
        sum_freq[window_sum] = sum_freq.get(window_sum, 0) + 1
            
    return count
    
if __name__ == "__main__":
    # nums = [1, 2, 3]
    # k = 3
    nums = [1]
    k = 0
    print("Output using Sliding Window:", subarray_sum_sliding_window(nums, k))
