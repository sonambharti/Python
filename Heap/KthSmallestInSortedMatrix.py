"""
# 378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Input Format :-
First Parameter - matrix, of size n x n
Second Parameter - k , kth element to be returned.

Output Format :-
Return the kth element in the sorted matrix.

Example 1 :-
Input:
3 3
1 5 9
10 11 13
12 13 15
8
Output:  
13
Explanation: 3 3 represents the size of the matrix. The elements in the matrix are 
[1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13.
Example 2 :-
Input: 
1 1
-5
1
Output:  
-5
"""

from collections import deque
from heapq import *

def KthSmallestInSortedMatrix(matrix, k):
    
    n = len(matrix)

    heap=[]
    
    for i in range(n*n):

        row = i // n

        col = i % n

        if k>0:

            heappush(heap,-1*matrix[row][col])
            k-=1

        else:
            
            if -1*heap[0] > matrix[row][col]:
                heappushpop(heap,-1*matrix[row][col])
    
    return -1 * heap[0]

if __name__ == '__main__':
	mat_dims = list(map(int, input().split()))
	matrix = [ [int(j) for j in input().split()] for i in range(mat_dims[0])]
	k = int(input())
	
	result = KthSmallestInSortedMatrix(matrix, k)
	print(result)
    # matrix = [[1, 5, 9], 
    # [10, 11, 13],
    # [12, 13, 15]]
    # k = 8
