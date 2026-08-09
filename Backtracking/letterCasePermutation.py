'''
784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
'''

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Time Complexity: O(n*2^n)
        # Space Complexity: O(n*2^n)
        n = len(s)
        res = []
        def backtrack(indx, path):
            if indx == n:
                res.append("".join(path))
                return

            # If current character is a digit,
            # there is only one choice
            if s[indx].isdigit():
                path.append(s[indx])
                backtrack(indx+1, path)
                path.pop()
            
            # If current character is a alphabet,
            # there is only one choice
            if s[indx].isalpha():
                # for lowercase
                path.append(s[indx].lower())
                backtrack(indx+1, path)
                path.pop()

                # for uppercase
                path.append(s[indx].upper())
                backtrack(indx+1, path)
                path.pop()

        backtrack(0, [])
        return res
                       
        
            
if __name__ == "__main__":
    s = "a1b2"
    
    res = Solution().letterCasePermutation(s)
    print(res)
    
