'''
# Find all anagrams in a substring

Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

from collections import defaultdict
def findAnagrams(s, p):
    n = len(s)
    m = len(p)

    if n < m:
        return []

    output = []

    counts_s, counts_p = defaultdict(int), defaultdict(int)

    # keeping track of s and p freq
    for i in range(len(p)):
        counts_p[p[i]] += 1
        counts_s[s[i]] += 1

    head, tail = 0, len(p)

    if counts_s == counts_p: # if freq of both s-subarr and p
        output.append(head)

    while tail < len(s):
        outgoing = s[head]
        incoming = s[tail]

        counts_s[outgoing] -= 1

        # This is to ensure I don't have dangling `0` values because I use `defaultdict`.
        # The dangling `0` values will cause the equality check to fail.
        if counts_s[outgoing] == 0:
            del counts_s[outgoing]

        counts_s[incoming] += 1

        if counts_s == counts_p:
            output.append(head + 1)

        head += 1
        tail += 1

    return output       
    
    
if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print("The start indexes of all anagrams: ", findAnagrams(s, p))
    
