'''
# Trapping Rain Water

Given an array arr[] with non-negative integers representing the height of blocks. If the width of
each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.

Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.
'''

def maxWater(arr):
    # code here
    n = len(arr)
    left = [0]*n
    right = [0]*n
    
    maxm = -float('inf')
    for i in range(n):
        maxm = max(arr[i], maxm)
        left[i] = maxm
        
    maxm = -float('inf')
    for i in range(n-1, 0, -1):
        maxm = max(arr[i], maxm)
        right[i] = maxm
        
    ans = 0
    minm = float('inf')
    for i in range(1, n-1):
        minm = min(left[i], right[i])
        ans += (minm - arr[i])
        
    return ans

if __name__ == "__main__":
    arr = [3, 0, 1, 0, 4, 0, 2]
    print("Maxm water can be trapped between the blocks during the rain: ", maxWater(arr))
    
