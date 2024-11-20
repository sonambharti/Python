'''
# 1338. Reduce Array Size to the half

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of
the old array.


Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

'''


import heapq

def minSetSize(arr):
    n = len(arr)
    freq = {}
    for el in arr:
        freq[el] = freq.get(el, 0) + 1

    freq = sorted(freq.values(), reverse=True)
    curr = 0
    res = 0
    for el in freq:
        curr += el
        res += 1
        if curr >= n//2:
            return res




def minSetSize_heapq(arr) :
    n = len(arr)
    freq = {}
    for el in arr:
        freq[el] = freq.get(el, 0) + 1
    
    l = []
    for _, v in freq.items():
        heapq.heappush(l, -v)
    cur = 0
    res = 0
    while True:
        cur -= heapq.heappop(l)
        res += 1
        if cur >= n // 2:
            return res
            
            
if __name__ == "__main__":
    arr = [7,7,7,7,7,7]
    res = minSetSize(arr)
    print("Minm size of array to remove: ", res)
    
    print("Minm size of array to remove using heapq: ", minSetSize_heapq([3,3,3,3,5,5,5,2,2,7]))
