'''
# Missing and Repeating

Given an unsorted array arr of of positive integers. One number 'A' from set {1, 2,....,n}
is missing and one number 'B' occurs twice in array. Find numbers A and B.

Note: The test cases are generated such that there always exists one missing and one repeating
number within the range [1,n].

Examples

Input: arr[] = [2, 2]
Output: 2 1
Explanation: Repeating number is 2 and smallest positive missing number is 1.
Input: arr[] = [1, 3, 3] 
Output: 3 2
Explanation: Repeating number is 3 and smallest positive missing number is 2.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

'''

class Solution:
    def findTwoElement(self, arr, n): 
        # Initialize variables to store repeating and missing numbers
        repeating = -1
        missing = -1
        
        # Iterate over the array to find the repeating number
        for i in range(n):
            # We are using the absolute value because the array values might be negative after previous iterations
            index = abs(arr[i]) - 1
            
            # If the value at the corresponding index is already negative, this is the repeating element
            if arr[index] < 0:
                repeating = abs(arr[i])
            else:
                # Mark the value at the index as visited (negate it)
                arr[index] = -arr[index]
        
        # Iterate over the array again to find the missing number
        for i in range(n):
            # The index that is not visited (positive value) is the missing number
            if arr[i] > 0:
                missing = i + 1
        
        return repeating, missing

# Example usage:
solution = Solution()
print(solution.findTwoElement([2, 2], 2))   # Output: (2, 1)
print(solution.findTwoElement([1, 3, 3], 3)) # Output: (3, 2)


