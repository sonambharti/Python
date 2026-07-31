'''
# 282. Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to 
insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant
expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Note that a number can contain multiple digits.

 

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
'''
class Solution:
    def helper(self, s, target, i, path, evaluate, residual, ans):
        if i == len(s):
            if evaluate == target:
                ans.append(path)
                return
        currStr = ""
        num = 0
        
        for j in range(i, len(s)):
            if (j > i and s[i]=='0'):
                break
            currStr += s[j]
            num = num * 10 + int(s[j])
            if i == 0:
                self.helper(s, target, j+1, path+currStr, num, num, ans)
            else:
                self.helper(s, target, j+1, path + "+" + currStr, evaluate + num, num, ans)
                self.helper(s, target, j+1, path + "-" + currStr, evaluate - num, -num, ans)
                self.helper(s, target, j+1, path + "*" + currStr, evaluate - residual + residual * num, residual * num, ans)
                
        
    def expressionAddOperators(self, s, target):
        ans = []
        self.helper(s, target, 0, "", 0, 0, ans)
        return ans

if __name__ == "__main__":
    num = "123"
    target = 6
    res = Solution().expressionAddOperators(num, target)
    print(f"All expressions to achieve target: {res}")
