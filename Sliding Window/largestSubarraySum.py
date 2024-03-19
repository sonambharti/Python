'''
Given an array arr[] of size n containing integers. The problem is to find the 
length of the longest sub-array having sum equal to the given value k.

Example 1:
Input: arr[] = { 10, 5, 2, 7, 1, 9 }, k = 15
Output: 4
Explanation: The sub-array is {5, 2, 7, 1}.

Example 2:
Input: arr[] = {-5, 8, -14, 2, 4, 12}, k = -5
Output: 5
'''

def brute_larg_subarray_sum(nums, k):
    maxLen = 0
    n = len(nums)
    for i in range(n):
        sum = 0 
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                maxLen = max(maxLen, j-i+1)

    return maxLen
    
def sliding_larg_subarray_sum(arr, k):
    maxLen = 0
    sum_index = {0: -1}  # Initialize with 0 to handle cases where cumulative sum equals k
    window_sum = 0
    
    for i, num in enumerate(arr):
        window_sum += num
        complement = window_sum - k
        
        if complement in sum_index:
            maxLen = max(maxLen, i - sum_index[complement])
        
        if window_sum not in sum_index:
            sum_index[window_sum] = i
            
    return maxLen
    
    
if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, 9]
    k = 15
    print("Output:", brute_larg_subarray_sum(nums, k))
    
    nums1 = [-5, 8, -14, 2, 4, 12]
    k1 = -5
    print("Output:", sliding_larg_subarray_sum(nums1, k1))
