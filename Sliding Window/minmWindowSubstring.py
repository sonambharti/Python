"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

"""


def minmWindowSubstring(s, t):
    # Initialize a dictionary to track the frequency of characters in t
    t_freq = dict()
    # from collections import Counter
    # t_freq = Counter(t)
    # print(t_freq)
    for char in t:
        # Increment the count for the letter in the dictionary
        t_freq[char] = t_freq.get(char, 0) + 1

    # Initialize left and right pointers for the sliding window
    left = 0
    right = 0

    # Initialize variables to track the minimum window substring
    min_len = float('inf')
    min_window = ""

    # Counter to track the number of characters in t that are currently in the window
    required_chars = len(t)
    
    while right < len(s):
        # If the current character is in t, decrement its frequency in the dictionary
        if s[right] in t_freq:
            t_freq[s[right]] -= 1
            if t_freq[s[right]] >= 0:
                # If the frequency becomes non-negative, it contributes to the required characters count
                required_chars -= 1
        
        # Move the right pointer to the right
        right += 1

        # Check if all characters in t are in the current window
        while required_chars == 0:
            # Update the minimum window substring if the current window is smaller
            if right - left < min_len:
                min_len = right - left
                min_window = s[left:right]

            # Move the left pointer to the right
            if s[left] in t_freq:
                t_freq[s[left]] += 1
                if t_freq[s[left]] > 0:
                    # If the frequency becomes positive, it means we need this character for the window
                    required_chars += 1

            left += 1

    return min_window


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    ans = minmWindowSubstring(s, t)
    print("Minimum window substring: ", ans)
    
        
    
