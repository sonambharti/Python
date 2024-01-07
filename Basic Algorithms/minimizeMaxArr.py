"""
You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.

 

Example 1:

Input: nums = [3,7,1,6]
Output: 5
"""

"""
Intuition

The previous element takes the fall for the bigger element.
The elements are getting equally distributed in a order.

Approach

Calculated average sum for every element in the given order.
The maximum average would be our answer.
"""

from math import ceil

def minimizeArrayValue(nums):
    sum = 0
    ans = 0
    n = len(nums)
    for i in range(n):
        sum += nums[i]
        avg = sum/(i+1)
        if avg > ans:
            ans = avg
    return ceil(ans)
    
nums = [3,7,1,6]
res = minimizeArrayValue(nums)
print(res)
