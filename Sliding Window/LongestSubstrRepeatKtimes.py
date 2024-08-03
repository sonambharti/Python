'''
# 395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring of s such that the 
frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


def longestSubstring(s, k):
    
    n = len(s)
    max_len = 0
    
    for unique_chars in range(1, 27):  # There are at most 26 different characters
        freq = {}
        left = 0
        right = 0
        num_unique = 0
        num_no_less_than_k = 0
        
        while right < n:
            # Expand the window by including s[right]
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
                num_unique += 1
            
            if freq[s[right]] == k:
                num_no_less_than_k += 1
            
            right += 1
            
            # Shrink the window from the left if the number of unique characters exceeds unique_chars
            while num_unique > unique_chars:
                if freq[s[left]] == k:
                    num_no_less_than_k -= 1
                
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                    num_unique -= 1
                
                left += 1
            
            # Update max_len if the current window is valid
            if num_unique == unique_chars and num_unique == num_no_less_than_k:
                max_len = max(max_len, right - left)
    
    return max_len

if __name__ == "__main__":
    # Example usage
    s1 = "aaabb"
    k1 = 3
    print("The length of the longest substring is:", longestSubstring(s1, k1))  # Output: 3
    
    s2 = "ababbc"
    k2 = 2
    print("The length of the longest substring is:", longestSubstring(s2, k2))  # Output: 5
