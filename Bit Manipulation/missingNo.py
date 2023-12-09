"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the 
range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""

def missingNumber(nums):
    n = len(nums)
    xor1=0
    xor2=0
    n=len(nums)
    for i in range(n):
        xor1^=nums[i]
        xor2^=i+1
    return xor1^xor2

n = [0,3,1]
res = missingNumber(n)
print("Missing no.:\n", res)
