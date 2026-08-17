'''
# 2865. Beautiful Towers I

You are given an array heights of n integers representing the number of bricks in 
n consecutive towers. Your task is to remove some bricks to form a mountain-shaped 
tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching
a maximum peak value with one or multiple consecutive towers and then non-increasing.

Return the maximum possible sum of heights of a mountain-shaped tower arrangement.

 

Example 1:

Input: heights = [5,3,4,1,1]
Output: 13
Explanation:
We remove some bricks to make heights = [5,3,3,1,1], the peak is at index 0.

Example 2:

Input: heights = [6,5,3,9,2,7]
Output: 22
Explanation:
We remove some bricks to make heights = [3,3,3,9,2,2], the peak is at index 3.

Example 3:

Input: heights = [3,2,5,5,2,3]
Output: 18
Explanation:
We remove some bricks to make heights = [2,2,5,5,2,2], the peak is at index 2 or 3
'''

from typing import List

class Solution:
    def maximumSumOfHeights_BruteForce(self, heights: List[int]) -> int: 
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        n = len(heights)
        ans = 0
        for peak in range(n):  
            total = heights[peak]
            curr = heights[peak]
            
            # left side of the peak
            for j in range(peak-1, -1, -1):
                curr = min(curr, heights[j])
                total += curr
            
            # right side of the peak
            curr = heights[peak]
            for j in range(peak+1, n):
                curr = min(curr, heights[j])
                total += curr
            ans = max(ans, total)
        return ans
        
        
    def maximumSumOfHeights_Optimized(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(heights)
        left = [0]*n
        right = [0]*n

        # calculate left contributions
        stack = []
        for i in range(n):  
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            
            if not stack:
                left[i] = heights[i] * (i+1)
            else:
                j = stack[-1]
                left[i] = left[j] + heights[i] * (i-j)

            stack.append(i)

        # calculate right contributions
        stack = []
        for i in range(n-1, -1, -1):  
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            
            if not stack:
                right[i] = heights[i] * (n-i)
            else:
                j = stack[-1]
                right[i] = right[j] + heights[i] * (j-i)
            stack.append(i)

        # Try every index as peak
        ans = 0
        for i in range(n):
            total = left[i] + right[i] - heights[i]
            ans = max(ans, total)
        return ans
                   
            
if __name__ == "__main__":
    heights = [3,2,5,5,2,3]
    
    res = Solution().maximumSumOfHeights_BruteForce(heights)
    print(res)
        
    res = Solution().maximumSumOfHeights_Optimized(heights)
    print(res)
    
