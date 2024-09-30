'''
# Minimal cost

There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one 
of the following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be 
jumped and cost will be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible 
total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum
Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.
'''

def minimizeCost(k, arr):
    # code here
    n = len(arr)
    dp = [float('infinity') for _ in range(n)]
    dp[0] = 0
    
    for i in range(n):
        for j in range(1, k+1):
            if i+j < n:
                dp[i+j] = min(dp[i+j], dp[i] + abs(arr[i] - arr[i+j]))
    return dp[n-1]
    
if __name__ == "__main__":
    k = 3
    arr = [10, 30, 40, 50, 20]
    res = minimizeCost(k, arr)
    print("The minimum possible total cost incurred before reaching the last stone is: ", res)
    
    
    
    
