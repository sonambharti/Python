"""
# Longest repeating character Replacement

You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character. You can perform
this operation at most k times.

Return the length of the longest substring containing the same letter you can 
get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        count[s[end]] = 1 + count.get(s[end], 0)
        window_len = end - start + 1
        maxcount = max(count.values())
        if (window_len - maxcount) > k:
            count[s[start]] -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len
    
    
if __name__ == "__main__":
    s = "AABABBA"
    k = 2  
    res = characterReplacement(s, k)
    
    print("Size of Longest repeating character after Replacement is: ", res)
