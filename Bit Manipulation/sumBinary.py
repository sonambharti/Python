"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
"""

def getSum(a, b):
    # return a if(b==0) else (self.getSum(a^b, (a&b)<<1))
    # ans = [int(i)for i in range(-1000, 1001)]
    # return ans[1000 + a+b]
    
    if not a or not b:
        return a if not b else b
        
    MASK = 0xffffffff
    while b:
        carry = a&b
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK
        
    if (a>>31) & 1:
        return ~(a^MASK)
    
    return a


a = 89
b = 78
res = getSum(a, b)
print("Sum = ", res)
