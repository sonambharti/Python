'''
# 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
'''

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time Complexity: O(4^n) fot the digits 7 & 9 where i has 4 options to choose
        # Space complexity: O(n*4^n)
      
        if not digits:
            return []
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(indx, path):
            if indx == len(digits):
                res.append("".join(path))
                return
            letters = mappings[digits[indx]]

            for ch in letters:
                path.append(ch)
                backtrack(indx+1, path)
                path.pop()
        res = []
        path = []
        backtrack(0, path)
        return res
        
            
            
if __name__ == "__main__":
    s = "23"
    
    res = Solution().letterCombinations(s)
    print(res)
    
