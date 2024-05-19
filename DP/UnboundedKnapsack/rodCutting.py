"""
Given a rod of length N inches and an array of prices, price[]. 
price[i] denotes the value of a piece of length i. Determine the 
maximum value obtainable by cutting up the rod and selling the pieces.

Note: Consider 1-based indexing.

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.
"""
def cutRod(price, n):
    #code here
    # This is variation of unbounded knapsack
    # length = [ i for i in range(1, n+1)]
    # m = len(length)
    # dp = [[-1] * (n+1) for _ in range(m+1)]
    # for i in range(m+1):
    #     for w in range(n+1):
    #         if i==0 or w==0:
    #             dp[i][w] = 0
    #         elif length[i-1] <= w:
    #             dp[i][w] = max(dp[i-1][w], price[i-1] + dp[i][w - length[i-1]])
    #         else:
    #             dp[i][w] = dp[i-1][w]
    # return dp[m][n]
    
    # Above code was giving TLE error for the redundant calculation in 2D array
    dp = [0] * (n + 1)

    # Iterate over each length of the rod
    for i in range(1, n + 1):
        # Calculate the maximum price for each length j
        for j in range(i, n + 1):
            dp[j] = max(dp[j], dp[j - i] + price[i - 1])
    
    return dp[n]

                
        
if __name__ == "__main__":
    N=8
    price= [3, 5, 8, 9, 10, 17, 17, 20]
    print("Maxm total price of rod using dp (unbounded knapsack): ", cutRod(price, N))
  
 
