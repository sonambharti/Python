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
# concept of prefix sum and a hashmap to keep track of the cumulative sum encountered
def subarray_sum(nums, k):
    count = 0
    sum_map = {0: 1}
    current_sum = 0

    for num in nums:
        current_sum += num
        complement = current_sum - k
        if complement in sum_map:
            count += sum_map[complement]
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1

    return count
    
if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    print("Output:", subarray_sum(nums, k))
