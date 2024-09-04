'''
# Count ways to N'th Stair(Order does not matter)

There are n stairs, and a person standing at the bottom wants to reach the top. The person can climb 
either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top 
(order does not matter).
Note: Order does not matter means for n = 4:- {1 2 1},{2 1 1},{1 1 2} are considered same.

Examples :

Input: n = 4
Output: 3
Explanation: Three ways to reach at 4th stair. They are {1, 1, 1, 1}, {1, 1, 2}, {2, 2}.
Input: n = 5
Output: 3
Explanation: Three ways to reach at 5th stair. They are {1, 1, 1, 1, 1}, {1, 1, 2, 1} and {1, 2, 2}.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
'''

def nthStair(n):
	# Code here
	
	return (n//2)+1
	
def nthStair_dp(n):
    if n==1 or n==2:
	    return n
	    
	# Create a DP array to store the number of ways to reach each stair
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 2
    # Populate the DP array using bottom-up approach
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 1 if i%2 == 0 else dp[i-1]
    return dp[n]

    
if __name__ == "__main__":
    n = 4
    print("Count the number of ways, the person can reach the top (order does not matter)", nthStair(n))
    res = nthStair_dp(n)
    print("Count the number of ways, the person can reach the top (order does not matter) using dp: ", res)

	
