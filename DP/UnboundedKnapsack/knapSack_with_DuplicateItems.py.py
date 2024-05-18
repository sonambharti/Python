"""
Given a set of N items, each with a weight and a value, represented by the array w 
and val respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. 
Return the maximum profit.
Note: Each item can be taken any number of times.

Example 1:

Input: 
N = 2
W = 3
val = {1, 1}
wt = {2, 1}
Output: 
3
Explanation: 
1.Pick the 2nd element thrice.
2.Total profit = 1 + 1 + 1 = 3. Also the total weight = 1 + 1 + 1  = 3 which is <= 3.
"""
def knapSack_with_DuplicateItems(N, W, val, wt):
    # code here
    dp = [0]*(W+1)
    for i in range(N):
        for w in range(wt[i], W+1):
            dp[w] = max(dp[w], val[i] + dp[w-wt[i]])
            
    return dp[W]
        
if __name__ == "__main__":
    # Example usage
    N = 2
    W = 3
    val = [1, 1]
    wt = [2, 1]
    print(knapSack_with_DuplicateItems(N, W, val, wt))
