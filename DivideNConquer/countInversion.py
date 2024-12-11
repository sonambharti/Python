'''

# Count Inversions

Given an array of integers arr[]. Find the Inversion Count in the array.
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array 
is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.

'''

import sys
sys.setrecursionlimit(10**6)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1 
    
    count = 0
    
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1 
        else:
            count += (mid - left + 1)
            temp.append(arr[right])
            right += 1 
            
    while (left <= mid):
        temp.append(arr[left])
        left += 1 
    while (right <= high):
        temp.append(arr[right])
        right += 1 
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]
    
    return count


def mergeSort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = (high + low) // 2
    count += mergeSort(arr, low, mid)
    count += mergeSort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count
    
    
if __name__ == "__main__":
    arr = [10,9,7,6,1,2,6,4]
    res = mergeSort(arr, 0, len(arr)-1)
    print(res)
