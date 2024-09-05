"""
# 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', return the length of 
the longest valid (well-formed) parentheses 
substring.
 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
"""


def longestValidParentheses(s):
    st = [-1]
    n = len(s)
    count = 0
    if n == 0:
        return 0
    for i in range(n):
        if s[i] == '(':
            st.append(i)
        else:
            st.pop()
            if len(st) == 0:
                st.append(i)
            else:
                count = max(count, i - st[-1])
    return count

    
# Example usage:
if __name__ == "__main__":
    s = ")()())"
    res = longestValidParentheses(s)
    print("The longest valid parentheses substring is: ", res)  
