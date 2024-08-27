"""
# 5. Longest Palindromic Substring


Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""
def longestPalindrome(s):
    n = len(s)
    res = ""
    resLeng = 0

    for i in range(n):
        # odd length
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > resLeng:
                res = s[l:r+1]
                resLeng = r - l + 1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > resLeng:
                res = s[l:r+1]
                resLeng = r - l + 1
            l -= 1
            r += 1
    return res

    
if __name__ == "__main__":
    string = "ababer"
    print(longestPalindrome(string))
