"""
Print the minimum no. of coins required from the coin set to make the sum ...
"""
import sys

def minmCoinChange(coins, sum):

    dp = [0] * (sum + 1)

    for i in range(1, sum + 1):

        dp[i] = sys.maxsize

        for c in range(len(coins)):
            if i - coins[c] >= 0:
                result = dp[i - coins[c]]

                if result != sys.maxsize:
                    dp[i] = min(dp[i], result + 1)

    return dp[sum]

# Driver program to test above function
if __name__ == '__main__':
	coins = [1, 2, 3]
	sum = 4
	res = minmCoinChange(coins, sum)
	print(res)
