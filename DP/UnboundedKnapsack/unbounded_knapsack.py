"""
Unbounded Knapsack (Repetition of items allowed)
 Given a knapsack weight W and a set of n items with certain value valid 
 and weight wti, we need to calculate minimum amount that could make up 
 this quantity exactly. This is different from classical Knapsack problem, 
 here we are allowed to use unlimited number  of instances of an item.
Examples:

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.
"""
def unbounded_knapSack(W, wt, val, n):
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
                dp[i][w] = max(val[i - 1] + dp[i][w - wt[i - 1]], dp[i - 1][w])
            # If the weight of the current item is greater than the knapsack capacity,
            # exclude the current item
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Return the maximum value that can be obtained using the items
    # and knapsack capacity
    return dp[n][W]
    
        
        
if __name__ == "__main__":
    N = 2
    W = 100
    values = [1,30]
    weight = [1,50]
    print("Maxm total value in knapsack using dp: ", unbounded_knapSack(W, weight, values, N))
  
 
