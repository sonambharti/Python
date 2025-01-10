'''
# Sum Pair closest to target

Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.
Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 
Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.
'''

def sumClosest(arr, target):
    # code here
    arr.sort()

    # Initialize pointers and variables
    left = 0
    right = len(arr) - 1
    closest_sum = float('inf')
    closest_pair = None

    while left < right:
        current_sum = arr[left] + arr[right]

        # Update the closest pair if the current sum is closer to the target
        if abs(target - current_sum) < abs(target - closest_sum):
            closest_sum = current_sum
            closest_pair = (arr[left], arr[right])

        # Move pointers based on the current sum
        if current_sum < target:
            left += 1
        else:
            right -= 1

    return closest_pair

    
if __name__ == "__main__":
    # Input array
    arr = [10, 30, 20, 5]
    target = 25
    
    # Sorting the array
    res = sumClosest(arr, target)
    print("Sum Pair Closest Sum: ", res)
    
    
