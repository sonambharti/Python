"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""
# Brute Force Approach
def minCostClimbingStairsBruteForce(cost):
    # Define a recursive function to explore all possible paths
    def climb(i):
        if i >= len(cost):
            return 0
        # Calculate the cost of climbing from the current step
        cost_one = cost[i] + climb(i + 1)
        cost_two = cost[i] + climb(i + 2)
        # Return the minimum cost of climbing from the current step
        return min(cost_one, cost_two)
    
    # Start climbing from step 0 or step 1
    return min(climb(0), climb(1))

# Dynamic Programming Approach
def minCostClimbingStairsDP(cost):
    n = len(cost)
    # Initialize a DP array to store the minimum cost to reach each step
    dp = [0] * (n + 1)
    # Base cases
    dp[0] = cost[0]
    dp[1] = cost[1]
    # Iterate through the array and calculate the minimum cost at each step
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    # The minimum cost to reach the top floor is the minimum of the cost at the last two steps
    return min(dp[n - 1], dp[n - 2])


def minCostClimbingStairsConstantSpace(cost):
    n = len(cost)
    # Base cases
    dp0 = cost[0]
    dp1 = cost[1]
    # Iterate through the array and calculate the minimum cost at each step
    for i in range(2, n):
        dp0, dp1 = dp1, cost[i] + min(dp0, dp1)
    # The minimum cost to reach the top floor is the minimum of the cost at the last two steps
    return min(dp0, dp1)

if __name__ == "__main__":
    # Example usage and comparison of approaches
    cost = [10, 15, 20]
    # Brute Force Approach
    print("Brute Force Approach:")
    print("Minimum cost to reach the top floor:", minCostClimbingStairsBruteForce(cost))
    # Dynamic Programming Approach
    print("Dynamic Programming Approach:")
    print("Minimum cost to reach the top floor:", minCostClimbingStairsDP(cost))
    
    cost = [10, 15, 20]
    print("Minimum cost to reach the top floor (Constant Space DP):", minCostClimbingStairsConstantSpace(cost))

