'''
# Indexes of Subarray Sum

Given an array arr[] containing only non-negative integers, your task is to find a continuous
subarray (a contiguous sequence of elements) whose sum equals a specified value target. You 
need to return the 1-based indices of the leftmost and rightmost elements of this subarray. 
You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].

Examples:

Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
'''

# using Hash map and prefix sum
def subarraySum(self, arr, target):
    # code here
    n = len(arr)
    if n == 0:
        return [-1]
    
    # Dictionary to store prefix sums
    prefix_sum = {}
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]

        # Check if current_sum matches the target
        if current_sum == target:
            return [1, i + 1]

        # Check if there is a prefix sum that matches current_sum - target
        if (current_sum - target) in prefix_sum:
            return [prefix_sum[current_sum - target] + 2, i + 1]

        # Store the current sum with its index
        prefix_sum[current_sum] = i
    return [-1]
    
    
def subarraySum_BruteForce(arr, target):
    # code here
    n = len(arr)
    if n == 0:
        return [-1]
    
    # Brute Force approach
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target:
                return [i+1, j+1]
    return [-1]
    
if __name__ == "__main__":
    # Input array
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    
    # Sorting the array
    res = countDistinct(arr, k)
    print("Indexes of Subarray Sum: ", res)
    
    
