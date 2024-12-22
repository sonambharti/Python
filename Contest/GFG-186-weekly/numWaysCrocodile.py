"""
# Reach Alice

Bob is standing on the left bank of a river, and Alice is on the right bank. To reach Alice,
Bob must cross the river by stepping on crocodiles forming a bridge from one bank to another. 
However, Bob must follow certain rules to avoid being attacked by the crocodiles.

There are n crocodiles in the river, arranged in a straight line. Each crocodile is either male
denoted by '0' or female denoted by '1'. A binary string s of length n is given where s[i] denotes
the type of the crocodile at i-th position. The rules for stepping on them are as follows:

* If Bob steps on a male crocodile at position i, he can jump to either the (i+1)th or (i+2)th
crocodile (if they exist).

* If Bob steps on a female crocodile at position i, he can only jump to the (i+1)th crocodile (if it exists).

Bob starts on the first crocodile and must reach the nth crocodile to meet Alice. Determine the number of 
distinct ways Bob can reach the nth crocodile. Since the answer can be very large, return it modulo 109+7.

Note: A way is considered to be distinct if the sequence of the indices of crocodiles stepped on is different.
"""
def numWays(s):
    # code here
    MOD = 10**9+7
    n = len(s)
    dp = [0]*n

    dp[0] = 1;

    # Fill the dp array
    for i in range(n):
        if (dp[i] == 0):
            continue # Skip if no way to reach this crocodile

        if (i + 1 < n):
            dp[i + 1] = (dp[i + 1] + dp[i]) % MOD # Jump to i+1

        if (s[i] == '0' and i + 2 < n):
            dp[i + 2] = (dp[i + 2] + dp[i]) % MOD # Jump to i+2 (only for male crocodiles)

    return dp[n - 1]

if __name__ == "__main__":
    s = "WLWLLLLL"
    print(isPossible(s))
