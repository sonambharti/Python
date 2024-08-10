"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

def findMedianSortedArrays(nums1, nums2):
    # If nums1 is longer than nums2, swap them to make sure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums1[i] < nums2[j - 1]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0: 
                max_of_left = nums2[j - 1]
            elif j == 0: 
                max_of_left = nums1[i - 1]
            else: 
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: 
                min_of_right = nums2[j]
            elif j == n: 
                min_of_right = nums1[i]
            else: 
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

    
if __name__ == "__main__":
    # Example usage
    nums1 = [1, 3]
    nums2 = [2]
    print("The median of the two sorted arrays is:", findMedianSortedArrays(nums1, nums2))  # Output: 2.0
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("The median of the two sorted arrays is:", findMedianSortedArrays(nums1, nums2))  # Output: 2.5
