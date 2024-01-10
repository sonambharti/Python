"""
# Longest substring without repeating characters
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    maxmlen = 0
    substr = set()
    l = 0
    for r in range(len(s)): 
        while s[r] in substr: 
            substr.remove(s[l]) 
            l+=1 
        substr.add(s[r])
        maxmlen = max(maxmlen, r-l+1)
    return maxmlen
    

if __name__ == "__main__":
    s = "pwwkew"
    res = lengthOfLongestSubstring(s)
    print("length of the longest substring without repeating characters = ", res)
    
