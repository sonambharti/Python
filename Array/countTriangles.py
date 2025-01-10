'''
# Count the number of possible triangles

Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements 
as lengths of three sides of the triangle. 

A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Examples:

Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a 
possible triangle.  

Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101], [10, 100, 101], 
[100, 101, 200] and [101, 200, 300]

Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.
'''

def countTriangles(arr):
    # code here
    n = len(arr)
    
    if n<3:
        return 0
    
    arr.sort()
    count = 0
    for k in range(n-1, 1, -1):
        i, j = 0, k-1
        while (i<j):
            if arr[i]+arr[j] > arr[k]:
                count += (j-i)
                j -= 1
            else:
                i += 1
    return count
        
        
    
if __name__ == "__main__":
    # Input array
    arr = [4, 6, 3, 7]
  
    res = countTriangles(arr)
    print("Count the number of possible triangles: ", res)
    
    
