'''
# 440. K-th Smallest in Lexicographical Order

Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].


Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second
smallest number is 10.

Example 2:

Input: n = 1, k = 1
Output: 1

'''


def count(curr):
    res = 0
    nei = curr + 1
    while curr <= n:
        nei = min(nei, n + 1)
        res += nei - curr
        curr *= 10
        nei *= 10
    return res
    
    
def findKthNumber(n, k):
    curr, i = 1, 1
    while i < k:
        steps = count(curr)
        if steps + i <= k:
            curr += 1
            i += steps
        else:
            curr *= 10
            i += 1
    return curr
    

if __name__ == "__main__":
    n = 13
    k = 2
    res = findKthNumber(n, k)
    print("The kth element in lexicographical order is: ", res)
    
    
