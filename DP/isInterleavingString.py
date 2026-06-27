'''
# 97. Interleaving String 

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings
respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 
'''

class Solution:
    # Brute force / Greedy approach
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        t = len(s3)
        i, j, k = 0, 0, 0
        progress = False
        while i < t:
            progress = False
            if i < t and j < n and s3[i] == s1[j]:
                while j < n:
                    if s3[i] != s1[j]:
                        break
                    i += 1
                    j += 1
                    progress = True

            if i < t and k < m and s3[i] == s2[k]:
                while k < m:
                    if s3[i] != s2[k]:
                        break
                    i += 1
                    k += 1
                    progress = True
            if not progress:
                return False       
        if i == t:
            return True
            

    def isInterleave_dp(self, s1: str, s2: str, s3: str) -> bool:

        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True

        # First column
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # First row
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill remaining table
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                take_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]

                take_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[i][j] = take_s1 or take_s2

        return dp[n][m]
        
if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    
    obj = Solution()
    
    ans = obj.isInterleave(s1, s2, s3)
    print(ans)
    
    s4 = "aabcc"
    s5 = "dbbca"
    s6 = "aadbbbaccc"
    ans2 = obj.isInterleave_dp(s4, s5, s6)
    print(ans2)

            
