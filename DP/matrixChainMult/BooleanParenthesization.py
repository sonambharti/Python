"""
# Boolean Parenthesization

Given a boolean expression s of length n with following symbols.
Symbols
    'T' ---> true
    'F' ---> false
and following operators filled between symbols
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer can be large, so return it with modulo 1003

Example 1:

Input: 
n = 7
s = T|T&F^T
Output: 
4
Explaination: 
The expression evaluates to true in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).

Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes n and s as input parameters and returns number of possible ways modulo 1003.

Expected Time Complexity: O(n3)
Expected Auxiliary Space: O(n2)
"""

def rec_countWays(n, s):
    MOD = 1003
    
    # Memoization dictionary
    memo = {}

    def rec_chainMatMult(s, i, j, bool_var):
        if i > j:
            return 0
        if i == j:
            if bool_var:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0
        
        if (i, j, bool_var) in memo:
            return memo[(i, j, bool_var)]
        
        ans = 0
        for k in range(i + 1, j, 2):
            lt = rec_chainMatMult(s, i, k - 1, True)
            lf = rec_chainMatMult(s, i, k - 1, False)
            rt = rec_chainMatMult(s, k + 1, j, True)
            rf = rec_chainMatMult(s, k + 1, j, False)
            
            if s[k] == '&':
                if bool_var:
                    ans += (lt * rt) % MOD
                else:
                    ans += (lt * rf + lf * rt + lf * rf) % MOD
            elif s[k] == '|':
                if bool_var:
                    ans += (lt * rt + lt * rf + lf * rt) % MOD
                else:
                    ans += (lf * rf) % MOD
            elif s[k] == '^':
                if bool_var:
                    ans += (lt * rf + lf * rt) % MOD
                else:
                    ans += (lt * rt + lf * rf) % MOD
        
        memo[(i, j, bool_var)] = ans % MOD
        return memo[(i, j, bool_var)]
    
    if n == 1:
        return 1 if s == 'T' else 0
    
    return rec_chainMatMult(s, 0, n - 1, True)

def dp_countWays(n, s):
    MOD = 1003
    
    # Create DP tables
    dp_true = [[0] * n for _ in range(n)]
    dp_false = [[0] * n for _ in range(n)]
    
    # Initialize the tables for the base cases
    for i in range(n):
        if s[i] == 'T':
            dp_true[i][i] = 1
            dp_false[i][i] = 0
        elif s[i] == 'F':
            dp_true[i][i] = 0
            dp_false[i][i] = 1

    # Fill the DP tables
    for length in range(3, n + 1, 2):
        for i in range(0, n - length + 1, 2):
            j = i + length - 1
            for k in range(i + 1, j, 2):
                operator = s[k]
                
                lt = dp_true[i][k - 1]
                lf = dp_false[i][k - 1]
                rt = dp_true[k + 1][j]
                rf = dp_false[k + 1][j]
                
                if operator == '&':
                    dp_true[i][j] += (lt * rt) % MOD
                    dp_false[i][j] += (lt * rf + lf * rt + lf * rf) % MOD
                elif operator == '|':
                    dp_true[i][j] += (lt * rt + lt * rf + lf * rt) % MOD
                    dp_false[i][j] += (lf * rf) % MOD
                elif operator == '^':
                    dp_true[i][j] += (lt * rf + lf * rt) % MOD
                    dp_false[i][j] += (lt * rt + lf * rf) % MOD

                dp_true[i][j] %= MOD
                dp_false[i][j] %= MOD

    return dp_true[0][n - 1]
    
    

if __name__ == "__main__":
    # Example usage:
    n = 7
    s = "T|T&F^T"
    print("The number of ways to parenthesize the expression to be true: ", rec_countWays(n, s))  # Output: 4
    
    n1 = 5
    s1 = "T^F|F"
    print("The number of ways to parenthesize the expression to be false: ", dp_countWays(n1, s1))
