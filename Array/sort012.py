'''
# Sort 0s, 1s and 2s

Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[]= [0, 2, 1, 2, 0]
Output: 0 0 1 2 2
Explanation: 0s 1s and 2s are segregated into ascending order.

Input: arr[] = [0, 1, 0]
Output: 0 0 1
Explanation: 0s 1s and 2s are segregated into ascending order.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

'''


def sortColors(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr


       
if __name__ == "__main__":
    # Example 1
    arr1 = [0, 2, 1, 2, 0]
    print("Sorted array:", sortColors(arr1))  # Output: [0, 0, 1, 2, 2]
    
    # Example 2
    arr2 = [2, 2, 0, 1, 0]
    print("Sorted array:", sortColors(arr2))  # Output: [0, 0, 1, 2, 2]
    
    # Example 3
    arr3 = [1, 1, 0, 0, 2, 2]
    print("Sorted array:", sortColors(arr3))  # Output: [0, 0, 1, 1, 2, 2]
