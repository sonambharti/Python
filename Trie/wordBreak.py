'''
# 139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

'''
from typing import List

class Trie:
    def __init__(self):
        # Constructor to initialize the Trie with an empty root node
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['$']={}


class Solution:
    def __init__(self):
        self.trie = Trie()

    def find_segments(self, s):
        # return `False` if the first char itself isn't present in Trie
        if s[0] not in self.trie.root:
            return False

        # Search the Trie for all possible space-separated word sequences
        # recursively using a stack and return `True` if all words
        # in `s` are found, else return `False`
        n = len(s)
        stack = [0]
        while len(stack) > 0 and len(stack) < 50:  # Note: 50 was arbitrarily chosen
            node = self.trie.root
            i = stack.pop()
            while i < n:
                ch = s[i]
                if ch in node:
                    if '$' in node:
                        stack.append(i)
                    node = node[ch]
                    i += 1
                else:
                    if '$' not in node and len(stack) == 0:
                        return False
                    elif '$' not in node:
                        break
                    node = self.trie.root
            if '$' in node:
                return True
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # trie = Trie()
        chars_in_dict = set()
        for word in wordDict:
            self.trie.insert(word)
            for c in word:
                chars_in_dict.add(c)
        
        chars_in_s = set(s)
        if chars_in_s.intersection(chars_in_dict) != chars_in_s:
            return False
        
        return self.find_segments(s)
        
if __name__ == "__main__":
    # s = "catsandog"
    # wordDict = ["cats","cat", "an", "dog"]
    s = "leetcode"
    wordDict = ["leet","code"]
    res = Solution().wordBreak(s, wordDict)
    print("s can be segmented into a space-separated sequence of one or more dictionary words or not: ", res)
        
