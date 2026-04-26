'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

 

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''

def leftMaxArr(height):
    n = len(height)
    left= []
    maxm = 0
    for i in range(0, n):
        maxm = max(maxm, height[i])
        left.append(maxm)
    return left
        
        
def rightMaxArr(height):
    n = len(height)
    right = [-1] * n 
    maxm = 0
    
    for i in range(n-1, -1, -1):
        maxm = max(maxm, height[i])
        right[i] = maxm
    return right

# Complexity = O(n)
def trapping_rain_water(height):
    n = len(height)
    leftMax = leftMaxArr(height)
    rightMax = rightMaxArr(height)
    ans = 0
    for i in range(n):
        ans += min(leftMax[i], rightMax[i]) - height[i]
    
    return ans

if __name__ == "__main__":
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    res = trapping_rain_water(height)
    print(f"Total amount of water trapped: {res}")
