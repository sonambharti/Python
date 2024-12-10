'''
# Min chars to add for Palindrome

Given a string s, the task is to find the minimum characters to be added at the front to make 
the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward.

Examples:

Input: s = "abc"
Output: 2
Explanation: Add 'b' and 'c' at front of above string to make it palindrome : "cbabc"

Input: s = "aacecaaaa"
Output: 2
Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"

'''


def computeLPS(s):
    n = len(s)
    lps = [0] * n
    length = 0
    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
    
def minChar(s):
    #Write your code here
        
    # Create a combined string with a delimiter
    rev_s = s[::-1]
    combined = s + '#' + rev_s
    lps = computeLPS(combined)
    
    # The minimum characters to add at the front
    return len(s) - lps[-1]
        
    
if __name__ == "__main__":
    s = "aacecaaaa"
    print(minChar(s))
