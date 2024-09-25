'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and 
two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside 
the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements 
denote the elements that should be merged, and the last n elements are set to 0 and should be 
ignored. nums2 has a length of n.

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
def inPlaceMergeSortArrays(nums1, nums2, m, n):
    # Last index of the merged array
    last = m + n - 1
    
    # Pointers for nums1 and nums2
    i, j = m - 1, n - 1

    # Merge nums1 and nums2, starting from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1

    # If there are any remaining elements in nums2, place them in nums1
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    
    # nums1 = [1] 
    # m = 1
    # nums2 = []
    # n = 0
    
    inPlaceMergeSortArrays(nums1, nums2, m, n)
    print("Merged Sorted Array: ", nums1)
