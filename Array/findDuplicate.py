"""
# 287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

"""
# Find Duplicate using dictionary or hash table
def findDuplicate_hash(nums):

    # using dictionary
    freq = {}
    for el in nums:
        if freq.get(el, 0) != 0:
            return el
        freq[el] = 1
        
    # for el in nums:
    #     freq[el] = freq.get(el, 0) + 1
    
    # for key, values in freq.items():
    #     if values > 1:
    #         return key
    return -1

        
        
# Fast-Slow Pointers Approach (Floyd's Cycle Detection)
def findDuplicate_2pointers(nums):
    #Your code here
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow
   
        
        
if __name__ == "__main__":
    nums = [1,3,4,2,2]
   
    res = findDuplicate_hash(nums)
    
    print("Repeated Element in given array = ", res)
    
    print("Repeated element using 2 pointers = ", findDuplicate_2pointers([3,1,3,4,2]))
    
    
  
