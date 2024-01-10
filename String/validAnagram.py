"""
# Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
def isAnagram(s: str, t: str) -> bool:
    # s = sorted(s)
    # t = sorted(t)

    s = "".join(sorted(s))
    t = "".join(sorted(t))

    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    # s = "rat"
    # t = "car"
    s = "anagram"
    t = "nagaram"
    res = isAnagram(s, t)
    print("Is Anagram valid or not: ", res)
    
