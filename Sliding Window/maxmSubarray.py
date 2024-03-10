"""
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. You can 
only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
"""

def Brute_maxSubarray(arr, k):
    maxmSubarr = []
    n = len(arr)
    for i in range(n-k+1):
        subarr = arr[i:i+k]
        j, maxm = 0, -10**9
        while j<k:
            maxm = max(maxm, subarr[j])
            j += 1
        maxmSubarr.append(maxm)
    return maxmSubarr
    

from collections import deque
    
def sliding_maxSubarray(nums, k):
    if not nums:
        return []

    n = len(nums)
    result = []
    window = deque()

    # Process the first k elements to initialize the window
    for i in range(k):
        # Remove all elements smaller than the current element from the end of the window
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    # Process the remaining elements
    for i in range(k, n):
        # Append the maximum element of the current window to the result
        result.append(nums[window[0]])

        # Remove elements outside the current window from the front of the window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove all elements smaller than the current element from the end of the window
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        window.append(i)

    # Append the maximum element of the last window to the result
    result.append(nums[window[0]])

    return result

        
if __name__ == "__main__":
    arr = [1,3,-1,-3,5,3,6,7]
    k= 3
    res = Brute_maxSubarray(arr, k)
    print("Bruteforce Maxm of subarray of size k: ", res)
    
    res = sliding_maxSubarray(arr, k)
    print("Sliding Window Maxm of subarray of size k: ", res)
