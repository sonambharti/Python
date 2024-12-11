'''

# Insert Intervals

Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith event and intervals is sorted in ascending order 
by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and 
newEnd represent the start and end of this interval.

Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending 
order by starti and intervals still does not have any overlapping intervals (merge overlapping 
intervals if necessary).

Examples:

Input: intervals = [[1,3], [4,5], [6,7], [8,10]], newInterval = [5,6]
Output: [[1,3], [4,7], [8,10]]
Explanation: The newInterval [5,6] overlaps with [4,5] and [6,7].

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,9]
Output: [[1,2], [3,10], [12,16]]
Explanation: The new interval [4,9] overlaps with [3,5],[6,7],[8,10].

'''


def insertInterval(intervals, newInterval):
	#Code here
    intervals.append(newInterval)
    intervals.sort()
    n = len(intervals)
    prev = 0
    
    for i in range(n):
        if intervals[i][0] <= intervals[prev][1]:
            intervals[prev][0] = min(intervals[prev][0], intervals[i][0])
            intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
        else:
            prev += 1
            intervals[prev][0] = intervals[i][0]
            intervals[prev][1] = intervals[i][1]
    
    for i in range(n-1, prev, -1):
        intervals.pop()
    
    return intervals

	
    
if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,9]
    res = insertInterval(intervals, newInterval)
    print(res)
    
    
