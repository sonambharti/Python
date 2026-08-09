'''
# 77. Combinations

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

'''

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for num in range(start, n+1):
                path.append(num)
                backtrack(num+1, path)
                path.pop()
        backtrack(1, [])
        return res
             
        
if __name__ == "__main__":
    n=1
    k=1
    res = Solution().combine(n, k)
    print(f"All the combinations of k number chosen from (1,n): \n{res}")
