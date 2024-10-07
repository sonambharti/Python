"""
You are given an integer array arr of length n and also given two integers
l and r (l <= r). You have to choose one element from subarray arr[l:r]
(l, r both are inclusive) and another element from the remaining array such that 
the product of these two elements should be maximum.

Note: 1-base indexing is used

Example 1:
    Input:
        n = 5
        arr = [3, 4, 7, 1, 2]
        l = 2, r = 4
    Output:
        21
    
    Explanation:
        Subarray arr[2:4] = [4, 7, 1] and remaining array = [3, 2] and for getting
        maximum product we choose 7 and 3 respectively and maximum product is 7 X 3 = 21.
        
        
"""


def maximumProduct(n, arr, l, r):
    # code here
    leftArr = []
    rightArr = []
    leftArr = arr[l-1:r]
    rightArr = [arr[i] for i in range(n) if i < l-1 or i >= r]
    
    # Edge case for empty right array (if l and r cover the entire array)
    if not rightArr:
        return max(leftArr)
        
    
    maxmLeft, maxmRight = - float('infinity'), - float('infinity')
    minmLeft, minmRight = float('infinity'), float('infinity')
    
    for el in leftArr:
        maxmLeft = max(maxmLeft, el)
        minmLeft = min(minmLeft, el)
        
    for el in rightArr:
        maxmRight = max(maxmRight, el)
        minmRight = min(minmRight, el)
    

        
    maxProd = [
        maxmLeft*maxmRight, 
        maxmLeft*minmRight, 
        minmLeft*maxmRight, 
        minmLeft*minmRight
        ]
    
    
    return max(maxProd)


if __name__ == "__main__":
    n = 5
    arr = [3, 4, 7, 1, 2]
    l = 2
    r = 4
    
    res = maximumProduct(n, arr, l, r)
    print("Maximum Product : ", res)
    
    
