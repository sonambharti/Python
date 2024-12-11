'''

# Non-overlapping Intervals

Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. 
Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.
Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: You need to remove two [1, 3] to make the rest of the intervals non-overlapping.

Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non overlapping.

'''


def minRemoval(intervals):
    # Code here
    n = len(intervals)
    # Sort intervals based on the start time in descending order
    intervals.sort(key=lambda x: -x[0])
    arr = intervals[0]
    count = 0
    
    for i in range(1, n):
        if arr[0] >= intervals[i][1]:
            arr=intervals[i]
        else:
            count += 1
    return count
    
if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    res = minRemoval(intervals)
    print(res)
    
    
