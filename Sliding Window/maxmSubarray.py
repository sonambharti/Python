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
        
if __name__ == "__main__":
    arr = [1,3,-1,-3,5,3,6,7]
    k= 3
    res = Brute_maxSubarray(arr, k)
    print("Maxm of subarray of size k: ", res)
    
