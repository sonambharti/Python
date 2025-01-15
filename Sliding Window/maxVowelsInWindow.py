'''
# 1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

def maxVowels_Brute(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    max_vowelFreq = 0
    for i in range(n-k+1):
        curr_freq = 0
        curr_window = s[i:i+k]
        for el in curr_window:
            if el in vowels:
                curr_freq += 1
        max_vowelFreq = max(max_vowelFreq, curr_freq)
    return max_vowelFreq
    
    
def maxVowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    max_vowelFreq = 0
    curr_freq = 0
    i, j = 0, 0
    while j<n:
        if s[j] in vowels:
            curr_freq += 1
        if (j-i+1 == k):
            max_vowelFreq = max(max_vowelFreq, curr_freq)
            if s[i] in vowels:
                curr_freq -= 1
            i += 1
        j += 1

    return max_vowelFreq
    
    
if __name__ == "__main__":
    s = "leetcode"
    k = 3
    print("Maximum Number of Vowels in a Substring of Given Length using Brute Force: ", maxVowels_Brute(s, k))
    print("Maximum Number of Vowels in a Substring of Given Length using sliding window: ", maxVowels(s, k))
