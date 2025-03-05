'''
# 647. Palindromic Strings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''

    
def countSubstrings_brute(s: str) -> int:
    def isPalindromic(s, start, end):
        while(start <= end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if isPalindromic(s, i, j):
                count += 1
    return count
        
        

def countSubstrings_optimal(s: str) -> int:
    '''
    If it is odd, expand left = (i-1) and right = (i+1)
    If it is even, expand left = (i) and right = (i+1)
    '''
    def isPalindromic(s, left, right):
        n = len(s)
        count = 0
        while(left>=0 and right<n) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    n = len(s)
    ans = 0

    for i in range(n):
        even = isPalindromic(s, i, i+1)
        odd = isPalindromic(s, i, i)
        ans += even + odd
    return ans
    
def countSubstrings_dp(s: str) -> int:
    n = len(s)
    palindrome = [[False] * n for _ in range(n)]
    ans = 0

    for i in range(n):
        palindrome[i][i] = True
        ans += 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            palindrome[i][i + 1] = True
            ans += 1

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
                palindrome[i][i + length - 1] = True
                ans += 1

    return ans

if __name__ == "__main__":
    s = "aaa"
    print("Brute force approach to count possible Palindromic substrings: ", countSubstrings_brute(s))
    print("Optimal approach to count possible Palindromic substrings: ", countSubstrings_optimal(s))
    print("count possible Palindromic substrings using DP: ", countSubstrings_dp(s))
    
