'''
# 16. 3 Sum closest

Given an integer array nums of length n and an integer target, find three integers 
in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

'''

import sys
    
def threeSumClosest(nums, target):
    n = len(nums)
    nums = sorted(nums)
    
    closest_sum = sys.maxsize
    for k in range(n-2):
        i = k + 1
        j = n - 1

        while i < j:
            curr_sum = nums[k] + nums[i] + nums[j]

            if (abs(target - curr_sum) < abs(target - closest_sum)):
                closest_sum = curr_sum
            if curr_sum < target:
                i += 1
            else:
                j -= 1
    return closest_sum

# Example usage:
if __name__ == "__main__":
    nums = [-1,2,1,-4]
    target = 1
    print(f"The sum of the three integer closest to target value {target}: ", threeSumClosest(nums, target))
    
    
