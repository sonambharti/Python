'''
# 643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return
this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
'''


def findMaxAverage_BruteForce(nums, k):
    n = len(nums)
    max_avg = -float('inf')
    for i in range(n-k+1):
        avg = sum(nums[i: i+k]) / k
        max_avg = max(max_avg, avg)

    return max_avg
    
def findMaxAverage_slidingWindow(nums, k):
    n = len(nums)
    max_avg = -float('inf')
    summ = sum(nums[:k])
    max_avg = summ / k  # Initialize max_avg with the first window's average

    # Slide the window across the array
    for i in range(k, n):
        summ += nums[i] - nums[i - k]  # Update the window sum
        max_avg = max(max_avg, summ / k)  # Update max_avg if the current average is higher

    return max_avg
    

if __name__ == "__main__":
    nums = [0,1,1,3,3]
    k = 4
    print("Brute Force approach to maximize Average Subarray: ", findMaxAverage_BruteForce(nums, k))
    print("Sliding Window approach to maximize Average Subarray: ", findMaxAverage_slidingWindow(nums, k))
    
