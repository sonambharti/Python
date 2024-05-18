"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step 
"""
import datetime
def Brute_climbStairs(n):
    if n==1 or n==2:
        return n
    return Brute_climbStairs(n - 1) + Brute_climbStairs(n - 2)
def climbStairsDP(n):
    if n==1 or n==2:
        return n
    # Create a DP array to store the number of ways to reach each stair
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    # Populate the DP array using bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
    
def climbStairsMatrixExponentiation(n):
    """
    This function calculates the number of ways to climb n stairs using matrix exponentiation.
    It uses a matrix to represent the recurrence relation and calculates the nth power of the matrix
    using exponentiation by squaring.
    """
    # Define the matrix
    matrix = [[1, 1], [1, 0]]

    # Calculate the nth power of the matrix using exponentiation by squaring
    def power(matrix, n):
        result = [[1, 0], [0, 1]]
        while n > 0:
            if n % 2 == 1:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            n //= 2
        return result

    # Define the multiplication function for matrices
    def multiply(a, b):
        x = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    x[i][j] += a[i][k] * b[k][j]
        return x
    # Calculate the number of ways to climb n stairs
    return power(matrix, n)[0][0]
    
if __name__ == "__main__":
    # No. of stairs
    n1 = 40
    n2 = 2
    start1 = datetime.datetime.now()
    res1 = Brute_climbStairs(n1)
    end1 = datetime.datetime.now()
    print("No. of ways to reach through Brute nth stair is: ", res1, "in ", end1-start1, "time.")
    
    start2 = datetime.datetime.now()
    res2 = climbStairsDP(n1)
    end2 = datetime.datetime.now()
    print("No. of ways to reach through DP nth stair is: ", res2,  "in ", end2-start2, "time.")
    
    start3 = datetime.datetime.now()
    res3 = climbStairsMatrixExponentiation(n1)
    end3 = datetime.datetime.now()
    print("No. of ways to reach through Matrix Exponentiation nth stair is: ", res3,  "in ", end3-start3, "time.")
    
