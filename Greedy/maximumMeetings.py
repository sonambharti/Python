'''
# N-meetings in one room

You are given timings of n meetings in the form of (start[i], end[i]) where start[i] 
is the start time of meeting i and end[i] is the finish time of meeting i. Return the
maximum number of meetings that can be accommodated in a single meeting room, when 
only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other 
chosen meeting.

Examples :

Input: n = 6, start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. 
The meetings are - (1, 2), (3, 4), (5,7) and (8,9)

Input: n = 3, start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.

'''
def maximumMeetings(n, start, end):
    # code here
    arr = [[-1] * 3 for _ in range(n)]
    
    for i in range(n):
        arr[i][0] = start[i]
        arr[i][1] = end[i]
        arr[i][2] = i + 1
        
    # print("Original array: ", arr)
    arr.sort(key=lambda x: x[1])
    # print("Array after sorting: ", arr)
    
    count = 1
    freeTime = arr[0][1]
    ds = [arr[0][2]] # Data structur which stores the order of the meeting perform
    
    for i in range(1, n):
        if arr[i][0] > freeTime:
            count += 1 
            freeTime = arr[i][1]
            ds.append(arr[i][2])
            
    return count

if __name__ == "__main__":
    n = 6
    start = [1, 3, 0, 5, 8, 5]
    end =  [2, 4, 6, 7, 9, 9]
    
    res = maximumMeetings(n, start, end)
    print("Maximum no of meetings in one room: ", res)
