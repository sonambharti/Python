"""
Print first negative from the K window of an array. And. if there is 
no negative number in a particular window then return 0 for that window.

Example:
Input:
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3 

Output: [-1, -1, -7, -15, -15, 0]
"""

def brute_force_firstNegNo(arr, k):
    n = len(arr)
    if k > n:
        return "Invalid window size given."
    res = []
    
    for i in range(n-k+1):
        sub_arr = arr[i:i+k]
        j = 0
        count = 0
        while j < k:
            if sub_arr[j] < 0:
                res.append(sub_arr[j])
                break
            else:
                count += 1 
            j+=1 
        if count == k:
            res.append(0)
    return res 
    
from collections import deque

def first_negative_in_window(arr, k):
    res = []
    n = len(arr)
    negArr = deque()
    
    for i in range(n):
        if negArr:
            x = i-k
            if negArr [0] == x:
                negArr.popleft()
        if arr[i] < 0:
            negArr.append(i)
        if i+1 >= k:
            if negArr:
                res.append(arr[negArr[0]])
            else:
                res.append(0)

    return res
    
if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3 
    res1 = brute_force_firstNegNo(arr, k)
    print("Array of first negatives in the window using Brute Force: ", res1)
    
    res2 = first_negative_in_window(arr, k)
    print("Array of first negatives in the window using sliding window: ", res2)
