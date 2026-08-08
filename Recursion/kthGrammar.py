'''
# 779. K-th Symbol in Grammar

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. 
Now in every subsequent row, we look at the previous row and replace each 
occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table
of n rows.

 

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01

Example 3:

Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 and k==1:
            return 0
        length = 2**(n-1)
        mid = length//2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k-mid)
"""
Explanation:

for n = 1: 0
for n = 2: 0 1
for n = 3: 0 1 1 0
for n = 4: 0 1 1 0 1 0 0 1
for n = 5: 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0
for n = 6: 0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0 1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 1

here for each n the length of grammar is 2^(n-1) => n = 2 (length of grammar = 2)
                                                 => n = 3 (length of grammar = 4)
and first half is the copy of the above row and second half is the negation/complement of above row.

"""
if __name__ == "__main__":
    n = 2
    k = 1
    
    res = Solution().kthGrammar(n, k)
    print(res)
        
