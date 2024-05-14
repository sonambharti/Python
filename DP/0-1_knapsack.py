"""
0-1 knapsack -> GFG 
You are given weights and values of N items, put these items in a knapsack of capacity W 
to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values 
and weights associated with N items respectively. Also given an integer W which represents 
knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of 
this subset is smaller than or equal to W. You cannot break an item, either pick the complete 
item or dont pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3.
"""

def rec_knapSack(W, wt, val, n):
    # code here
    if n == 0 or W == 0:
        return 0
    
    if wt[n-1] > W:
        return rec_knapSack(W, wt, val, n-1)
    else:
        return max(val[n-1] + rec_knapSack(W-wt[n-1], wt, val, n-1), rec_knapSack(W, wt, val, n-1))

def memoize_knapSack(W, wt, val, n):
    # code here
    dp = [[-1] * (W+1) for _ in range(n+1)]
    def rec_knapSack(W, wt, val, n):
        if n == 0 or W == 0:
            return 0
        if dp[n][W] != -1:
            return dp[n][W]
        
        if wt[n-1] <= W:
            dp[n][W] = max(val[n-1] + rec_knapSack(W-wt[n-1], wt, val, n-1), rec_knapSack(W, wt, val, n-1))
        elif wt[n-1] > W:
            dp[n][W] = rec_knapSack(W, wt, val, n-1)
        return dp[n][W]
    return rec_knapSack(W, wt, val, n)
    
    
def knapSack(W, wt, val, n):
    # code here
    dp = [[-1] * (W + 1) for _ in range(n + 1)]

    # Build the dp table bottom-up
    for i in range(n + 1):
        for w in range(W + 1):
            # Base case: if either number of items is 0 or knapsack capacity is 0,
            # the maximum value that can be obtained is 0
            if i == 0 or w == 0:
                dp[i][w] = 0
            # If the weight of the current item is less than or equal to
            # the knapsack capacity, consider including it
            elif wt[i - 1] <= w:
                # Choose the maximum value between including the current item
                # and excluding the current item
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            # If the weight of the current item is greater than the knapsack capacity,
            # exclude the current item
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Return the maximum value that can be obtained using the items
    # and knapsack capacity
    return dp[n][W]
    
        
        
if __name__ == "__main__":
    N = 3
    W = 3
    values = [1,2,3]
    weight = [4,5,6]
    print("Maxm total value in knapsack using reccursion: ", rec_knapSack(W, weight, values, N))
    print("Maxm total value in knapsack using memoization: ", memoize_knapSack(W, weight, values, N))
    print("Maxm total value in knapsack using dp: ", knapSack(W, weight, values, N))
  
