'''
# Longest Consecutive Subsequence

Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements 
in the subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive 
subsquence.

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.
'''

from typing import List

class BruteForce:
    def linearSearch(self, arr, key):
        n = len(arr)
        for i in range(n):
            if arr[i] == key:
                return True
        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        for i in range(n):
            x = nums[i]
            count = 1
            while (self.linearSearch(nums, x+1) == True):
                x = x + 1
                count = count + 1
            longest = max(longest, count)
        
        return longest


import sys
def longestConsecutive_better(nums):
    n = len(nums)
    nums.sort()
    lastSmall = - sys.maxsize
    longest = 0
    count = 1
    for i in range(n):
        if nums[i] - 1 == lastSmall:
            count = count + 1 
            lastSmall = nums[i]
        elif nums[i] != lastSmall:
            count = 1 
            lastSmall = nums[i]
        longest = max(longest, count)
        
    return longest
    
    
def longestConsecutive_optimal(nums):
    n=len(nums)
    longest=1 
    if n==0:
        return 0 
    s=set(nums)
    for i in s:
        if i-1 not in s: # search in a set takes O(1) as it uses hash table to store elements
            cnt=1 
            x=i 
            while x+1 in s:
                cnt+=1 
                x+=1 
            longest=max(longest,cnt)
    return longest
        
        
if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    Bobj = BruteForce()
    print("The longest consecutive subsequence by Brute Force: ", Bobj.longestConsecutive(nums))
    
    print("The longest consecutive subsequence in better way: ", longestConsecutive_better(nums))
    
    print("The longest consecutive subsequence in optimal: ", )
