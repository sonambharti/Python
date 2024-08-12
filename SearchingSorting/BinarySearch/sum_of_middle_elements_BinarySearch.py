"""
# Sum of Middle elements of two sorted arrays

Given 2 sorted integer arrays arr1 and arr2 of the same size. Find the sum of the 
middle elements of two sorted arrays arr1 and arr2.

Examples:

Input: arr1 = [1, 2, 4, 6, 10], arr2 = [4, 5, 6, 9, 12]
Output: 11
Explanation: The merged array looks like [1, 2, 4, 4, 5, 6, 6, 9, 10, 12]. 
Sum of middle elements is 11 (5 + 6).

Input: arr1 = [1, 12, 15, 26, 38], arr2 = [2, 13, 17, 30, 45]
Output: 32
Explanation: The merged array looks like [1, 2, 12, 13, 15, 17, 26, 30, 38, 45]. 
Sum of middle elements is 32 (15 + 17).
"""

def sum_of_middle_elements_BinarySearch(arr1, arr2):
    # code here
    
    n = len(arr1)

    # Helper function to find the kth element in the union of arr1 and arr2
    def findKthElement(arr1, arr2, k):
        if len(arr1) == 0:
            return arr2[k]
        if len(arr2) == 0:
            return arr1[k]
        if k == 0:
            return min(arr1[0], arr2[0])

        mid1 = len(arr1) // 2
        mid2 = len(arr2) // 2

        if mid1 + mid2 < k:
            if arr1[mid1] > arr2[mid2]:
                return findKthElement(arr1, arr2[mid2+1:], k - mid2 - 1)
            else:
                return findKthElement(arr1[mid1+1:], arr2, k - mid1 - 1)
        else:
            if arr1[mid1] > arr2[mid2]:
                return findKthElement(arr1[:mid1], arr2, k)
            else:
                return findKthElement(arr1, arr2[:mid2], k)
                
    # Find the middle elements
    mid1 = findKthElement(arr1, arr2, n - 1)
    mid2 = findKthElement(arr1, arr2, n)

    return mid1 + mid2
    
    
    
def sum_of_middle_elements_Merge(arr1, arr2):
    # code here
    
    m = len(arr1)
    n = len(arr2)
    
    def merge(arr1, arr2, m, n):
        Lptr, Rptr = 0, 0

        arr =[]
        while Lptr < m and Rptr < n :
            if (arr1[Lptr] < arr2[Rptr]):
                arr.append(arr1[Lptr])
                Lptr += 1 
            else:
                arr.append(arr2[Rptr])
                Rptr += 1 
    
        while Lptr < m :
            arr.append(arr1[Lptr])
            Lptr += 1 
        
        while Rptr < n :
            arr.append(arr2[Rptr])
            Rptr += 1 
            
        return arr
        
    arr = merge(arr1, arr2, m, n)
    mid = (m+n)//2
    
    res = arr[mid-1] + arr[mid]
    
    return res
    
    
    
if __name__ == "__main__":
    arr1 = [1, 2, 4, 6, 10]
    arr2 = [4, 5, 6, 9, 12]
    res = sum_of_middle_elements_Merge(arr1, arr2)
    # res = sum_of_middle_elements_BinarySearch(arr1, arr2)
    print("Sum of Middle elements of two sorted arrays = ", res)
