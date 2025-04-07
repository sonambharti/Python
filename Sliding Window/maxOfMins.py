'''
# Max of min of every window size

Given an array of integers arr[], the task is to find the maximum of the minimum values for 
every possible window size in the array, where the window size ranges from 1 to arr.size().

More formally, for each window size k, determine the smallest element in all windows of size k,
and then find the largest value among these minimums where 1<=k<=arr.size().

Examples :

Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10] 
Explanation: 
1. First element in output indicates maximum of minimums of all windows of size 1. Minimums of
windows of size 1 are [10], [20], [30], [50], [10], [70] and [30]. Maximum of these minimums is 70. 
2. Second element in output indicates maximum of minimums of all windows of size 2. Minimums of 
windows of size 2 are [10], [20], [30], [10], [10], and [30]. Maximum of these minimums is 30. 
3. Third element in output indicates maximum of minimums of all windows of size 3. Minimums of 
windows of size 3 are [10], [20], [10], [10] and [10]. Maximum of these minimums is 20. 
Similarly other elements of output are computed.

Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]
Explanation: First element in output indicates maximum of minimums of all windows of size 1. 
Minimums of windows of size 1 are [10] , [20] , [30]. Maximum of these minimums are 30 and 
similarly other outputs can be computed.
'''

from collections import deque

# Got TLE as complexity O(n^2)
class Solution:
    def helperMaxmMinm(self, arr, k):
        if not arr or k <= 0:
            return []
    
        minmArr = []
        window = deque()  # stores indices of elements in the current window
    
        for i in range(len(arr)):
            # Remove indices that are out of the current window
            while window and window[0] <= i - k:
                window.popleft()
    
            # Remove indices whose corresponding values are greater than current element
            while window and arr[window[-1]] >= arr[i]:
                window.pop()
    
            window.append(i)
    
            # Append the minimum for the current window
            if i >= k - 1:
                minmArr.append(arr[window[0]])
        return max(minmArr)
        
    def maxOfMins(self, arr):
       # code here
        n = len(arr)
        res = []
        for i in range(1, n):
            res.append(self.helperMaxmMinm(arr, i))
        return res


# monotonic stacks and the idea of "Next Smaller Element" (NSE) and "Previous Smaller Element" (PSE) 
def maxOfMins_optimized(arr):
    n = len(arr)
    left = [-1] * n  # previous smaller element
    right = [n] * n  # next smaller element
    stack = []

    # Compute previous smaller elements
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    # Reset stack to compute next smaller elements
    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # Initialize result array with minimums
    res = [0] * (n + 1)

    for i in range(n):
        length = right[i] - left[i] - 1
        res[length] = max(res[length], arr[i])

    # Fill remaining entries from right to left
    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])

    return res[1:]  # ignore index 0


        
if __name__ == "__main__":
    arr = [10, 20, 30, 50, 10, 70, 30]
    obj = Solution()
    res = obj.maxOfMins(arr)
    print("Brute Force Sliding Window: ", res)
    
    print("Optimum Approach to find Max of minimum of the array: ", maxOfMins_optimized(arr))
    
           
