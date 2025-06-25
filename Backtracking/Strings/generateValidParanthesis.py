'''
# Generate Paranthesis

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
 
'''

from typing import List

class Solution:
    def back_track(self, n, st, res, open_count, close_count):
        # valid IIF close_count = open_count = n. Our base case.
        if open_count == close_count == n:
            valid = "".join(st)
            res.append(valid)
            return
        
        # only add open parenthesis if open_count < n
        if open_count < n:
            st.append("(")
            self.back_track(n, st, res, open_count+1, close_count)
            st.pop()

        # only add close paranthesis if close_count < open_count
        if close_count < open_count:
            st.append(")")
            self.back_track(n, st, res, open_count, close_count+1)
            st.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        st = []
        res = []
        self.back_track(n, st, res, 0, 0)
        return res
        
if __name__ == "__main__":
    n = 3
    obj = Solution()
    print("The different possible parenthesis: \n", obj.generateParenthesis(n))

