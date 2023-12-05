"""
Given an array of intervals such that interval[i] = [starti, endi], 
return the minimum number of intervals needed to remove for making 
the remaining intervals non-overlapping.


"""

def nonOverlapInterval(interval):
    interval = sorted(interval, key = lambda x: x[0])
    
    count = 0

    curr = interval[0]    

    for nxt in interval[1:]:
        if curr[1]<=nxt[0]:
            curr[1] = nxt[1]
        else:
            count+=1
            curr[1] = min(curr[1],nxt[1])
            
    return count

interval = [[1, 2], [2, 3], [3, 4], [1, 3]]
res = nonOverlapInterval(interval)
print("Total no. of Overlapped interval to be removed: ", res)
