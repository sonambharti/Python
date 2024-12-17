'''
# The Painter's Partition Problem-II

Dilpreet wants to paint his dog's home that has n boards with different lengths. The length of ith board is
given by arr[i] where arr[] is an array of n integers. He hired k painters for this work and each painter 
takes 1 unit time to paint 1 unit of the board.

Return the minimum time to get this job done if all painters start together with the constraint that any painter
will only paint continuous boards, say boards numbered [2,3,4] or only board [1] or nothing but not boards [2,4,5].

Examples:

Input: arr[] = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The most optimal way will be: Painter 1 allocation : [5,10], Painter 2 allocation : [30], Painter 3 
allocation : [20,15], Job will be done when all painters finish i.e. at time = max(5+10, 30, 20+15) = 35

Input: arr[] = [10, 20, 30, 40], k = 2
Output: 60
Explanation: The most optimal way to paint: Painter 1 allocation : [10,20,30], Painter 2 allocation : [40], Job will
be complete at time = 60

Input: arr[] = [100, 200, 300, 400], k = 1
Output: 1000
Explanation: There is only one painter, so the painter must paint all boards sequentially. The total time taken will
be the sum of all board lengths, i.e., 100 + 200 + 300 + 400 = 1000.
'''
import sys
def isPossible(arr, mid, k):
    count = 1
    min_sum = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            return 0
        elif (min_sum + arr[i] > mid):
            count += 1
            min_sum = arr[i]
            if count > k:
                return 0
        else:
            min_sum += arr[i]
    return 1
    
    
def minTime (arr, k):
    #code here
    
    n = len(arr)
    summ = 0
    mxm = 0
    for i in range(n):
        summ += arr[i]
        mxm = max(mxm, arr[i])
        
    low = mxm
    high=summ
    ans = sys.maxsize
    
    while (low <= high):
        mid = low + (high - low) // 2
        if isPossible(arr, mid, k):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    return ans
    
    
def minTime_optimize(arr, k):
    #code here
    def isPossible(arr, mid, k):
        count = 1
        min_sum = 0
        for i in range(len(arr)):
            min_sum += arr[i]
            if (min_sum > mid):
                count += 1
                min_sum = arr[i]
                    
        return count<=k
    
    n = len(arr)
    summ = 0
    mxm = 0
    for i in range(n):
        summ += arr[i]
        mxm = max(mxm, arr[i])
        
    low = mxm
    high=summ
    ans = high
    
    while (low <= high):
        mid = low + (high - low) // 2
        if isPossible(arr, mid, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
    
    
    
if __name__ == "__main__":
    arr = [5, 10, 30, 20, 15]
    k = 3
    res = minTime(arr, k)
    
    print("the minimum time to get this job done if all painters start together: ", res)
    
    print("the minimum time to get this job done if all painters start together: ", minTime_optimize(arr, k))
    
