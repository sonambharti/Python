"""
Given an 0-indexed array of integers arr[] of size n, find its peak element. 
An element is considered to be peak if it's value is greater than or equal 
to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Example 1:

Input: 
n = 3
arr[] = {1, 2, 3}
Peak element's index: 2
Output: 
1
"""
def peakElement(arr, n):
    # Code here
    start = 0
    end = n-1
    
    while start <= end:
        mid = start + (end - start) // 2
        if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            break
        if(mid > 0 and arr[mid - 1] > arr[mid]):
            end = mid - 1
        else:
            start = mid+1
    return mid
    
if __name__ == "__main__":
    n = 3
    arr = [1, 2, 3]
    index = peakElement(arr, n)
    print("Peak element at index: ", index)
    flag = False
    if index<0 or index>=n:
        flag = False
    else:
        if index == 0 and n==1:
            flag = True
        elif index==0 and arr[index]>=arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>=arr[index-1]:
            flag = True
        elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
            flag = True
        else:
            flag = False

    if flag:
        print(1)
    else:
        print(0)
