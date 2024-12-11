'''

# Overlapping Intervals

Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to 
merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, 
[1,3] and [2,4] which on merging will become [1,4]. Therefore we will return 
[[1,4], [6,8], [9,10]].

Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: In the given intervals all the intervals overlap with the interval [1,9]. 
Therefore we will return [1,9].

'''
def mergeOverlap(arr):
	#Code here
	arr.sort()
	merge=[arr[0]]
	for i in range(len(arr)):
	    lmerge=merge[-1]
	    if lmerge[1]>=arr[i][0]:
	        lmerge[1]=max(lmerge[1],arr[i][1])
	    else:
	        merge.append(arr[i])
	return merge
    
if __name__ == "__main__":
    arr = [[6,8],[1,9],[2,4],[4,7]]
    res = mergeOverlap(arr)
    print(res)
