'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and 
two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

'''
def mergeSortArrays(nums1, nums2, m, n):
    Lptr, Rptr = 0, 0

    arr =[]
    while Lptr < m and Rptr < n :
        if (nums1[Lptr] < nums2[Rptr]):
            arr.append(nums1[Lptr])
            Lptr += 1 
        else:
            arr.append(nums2[Rptr])
            Rptr += 1 

    while Lptr < m :
        arr.append(nums1[Lptr])
        Lptr += 1 
    
    while Rptr < n :
        arr.append(nums2[Rptr])
        Rptr += 1 
    
    return arr
    
if __name__ == "__main__":
    # nums1 = [1,2,3]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    
    nums1 = [1] 
    m = 1
    nums2 = []
    n = 0
    
    res = mergeSortArrays(nums1, nums2, m, n)
    print("Merged Sorted Array: ", res)
