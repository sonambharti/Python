"""
# 20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
"""

def isValid(s):
    stack = []
    matching_paren = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_paren.values():
            stack.append(char)
        elif char in matching_paren.keys():
            if stack == [] or stack.pop() != matching_paren[char]:
                return False
        else:
            return False
    
    return stack == []

if __name__ == "__main__":
  s = "(){}}{"
  res = isValid(s)
  print("Is the given paranthesis string valid or not:", res)
