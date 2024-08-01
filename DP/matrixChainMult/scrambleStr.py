"""
# 87. Scramble String
We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it 
to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s 
may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, 
return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index 
each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second 
substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""

def rec_isScramble(s1, s2):
    n = len(s1)
    if s1 == s2:
        return True
    if n <= 1:
        return False
    if sorted(s1) != sorted(s2):  # quick check to eliminate obviously non-scramble strings
        return False
    flag = False
    for i in range(1, n):
        condn1 = ((rec_isScramble(s1[:i], s2[:i]) == True) and (rec_isScramble(s1[i : ], s2[i : ]) == True))
        condn2 = ((rec_isScramble(s1[:i], s2[-i:]) == True) and (rec_isScramble(s1[i:], s2[:-i]) == True))
        if (condn1 or condn2):
            flag = True
    return flag

memo = {}
def mem_isScramble(s1, s2):
    global memo
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    
    if s1 == s2:
        return True
    
    if sorted(s1) != sorted(s2):  # quick check to eliminate obviously non-scramble strings
        return False
    
    n = len(s1)
    if n <= 1:
        return False

    for i in range(1, n):
        # Check if the two substrings are scrambled without swapping
        if (mem_isScramble(s1[:i], s2[:i]) and mem_isScramble(s1[i:], s2[i:])) or \
           (mem_isScramble(s1[:i], s2[-i:]) and mem_isScramble(s1[i:], s2[:-i])):
            memo[(s1, s2)] = True
            return True
        
        memo[(s1, s2)] = False
        return False
    
def dp_isScramble(s1, s2):
    n = len(s1)
    if n != len(s2):
        return False
    
    # dp[i][j][k] will be True if s1[i:i+k] is a scramble of s2[j:j+k]
    dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
    
    # Initialization for the case where the length of the substring is 1
    for i in range(n):
        for j in range(n):
            dp[i][j][1] = (s1[i] == s2[j])
    
    # Fill the DP table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):  # start index in s1
            for j in range(n - length + 1):  # start index in s2
                for k in range(1, length):  # split point
                    if (dp[i][j][k] and dp[i + k][j + k][length - k]) or \
                       (dp[i][j + length - k][k] and dp[i + k][j][length - k]):
                        dp[i][j][length] = True
                        break
    
    return dp[0][0][n]

if __name__ == "__main__":
    s1 = "abcde"
    s2 = "caebd"
    # res = rec_isScramble(s1, s2)
    # res = mem_isScramble(s1, s2)
    res = dp_isScramble(s1, s2)
    print("Is given string Scramble or not: ", res)
