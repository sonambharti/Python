'''
# Wildcard Pattern Matching

Given two strings pattern and str which may be of different size, You have to return 1 
if the wildcard pattern i.e. pattern, matches with str else return 0. All characters 
of the string str and pattern always belong to the Alphanumeric characters.

The wildcard pattern can include the characters ? and *
‘?’ – matches any single character.
‘*’ – Matches any sequence of characters (including the empty sequence).

Note: The matching should cover the entire str (not partial str).

Examples:

Input: pattern = "ba*a?", str = "baaabab"
Output: 1
Explanation: replace '*' with "aab" and 
'?' with 'b'.

Input: pattern = "a*ab", str = "baaabab"
Output: 0
Explanation: Because in string pattern character 'a' at first position,
pattern and str can't be matched. 
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)


'''
def wildCard_recursion(i, j, pattern, string):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        for star in range(i+1):
            if pattern[star] != '*':
                return False
        return True
        
    if pattern[i] == string[j] or pattern[i] == '?':
        return wildCard_recursion(i-1, j-1, pattern, string)
        
    
    if pattern[i] == '*':
        return wildCard_recursion(i-1, j, pattern, string) or wildCard_recursion(i, j-1, pattern, string)
    return False
    
    
def wildCard_dp(pattern, string):
    # Code here
    n = len(pattern)
    m = len(string)
    
    # Create a 2D DP table
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Base case: both pattern and string are empty
    dp[0][0] = True
    
    # Fill the first row where the string is empty
    # Only '*' in the pattern can match an empty string
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = False
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                # Characters match or pattern has '?', take the diagonal value
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                # '*' can match any sequence, so we check both:
                # 1. '*' matches 0 characters (dp[i-1][j])
                # 2. '*' matches 1 or more characters (dp[i][j-1])
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                # Characters do not match
                dp[i][j] = False
    
    # The answer is stored in dp[n][m]
    return dp[n][m]
        

if __name__ == "__main__":
    pattern = "ba*a?"
    string = "baaabab"
    n = len(pattern)
    m = len(string)
    res = wildCard_recursion(n-1, m-1, pattern, string)
    print("If the wildcard pattern matches or not: ", res)
    
    res1 = wildCard_dp(pattern, string)
    print("If the wildcard pattern matches or not: ", res1)
    
        
