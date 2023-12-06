"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

def insertInterval(intervals, newInterval):
    
    intervals.append(newInterval)
    intervals = sorted(intervals, key = lambda x : x[0])
    res = []
    for start, end in intervals:
        if not res or start > res[-1][1]:
            res.append([start, end])
        elif start <= res[-1][1] and end > res[-1][1]:
            res[-1][1] = end
    
    return res


interval = [[1, 2], [2, 3], [5, 6]]
newInterval = [3, 5]
res = insertInterval(interval, newInterval)
print("Total no. of Overlapped interval to be removed: ", res)
