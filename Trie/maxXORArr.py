"""
# Maximum XOR of two numbers in an array

Given an array arr[] of non-negative integers of size n. Find the maximum possible 
XOR between two numbers present in the array.

Examples:

Input: arr[] = [25, 10, 2, 8, 5, 3]
Output: 28
Explanation: The maximum possible XOR is 5 ^ 25 = 28.
Input: arr[] = [1, 2, 3, 4, 5, 6, 7]
Output: 7
Explanation : The maximum possible XOR is 1 ^ 6 = 7.

"""

# Brute Force Approach - O(n^2)
def maxXor_Brute(arr):
    #code here
    n = len(arr)
    maxm = -float('inf')
    for i in range(n):
        for j in range(i, n):
            xor = arr[i] ^ arr[j]
            maxm = max(maxm, xor)
    return maxm
    
    
# Optimized Code using Bit Magic (Prefix XOR + Set) - O(n)
def maxXor_BitMagic(arr):
    max_xor = 0
    mask = 0
    prefixes = set()

    for i in range(31, -1, -1):  # From MSB to LSB
        mask |= (1 << i)
        prefixes = {num & mask for num in arr}

        # Try to set the current bit in max_xor to 1
        candidate = max_xor | (1 << i)
        found = False
        for p in prefixes:
            if (candidate ^ p) in prefixes:
                found = True
                break

        if found:
            max_xor = candidate  # keep the bit set if it works

    return max_xor
    
    
# Optimize Approach using Trie 
class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):  # 32-bit representation
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def findMaxXor(self, root, num):
        node = root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit, node)
        return max_xor

    def maxXor(self, arr):
        root = TrieNode()
        max_result = 0
        self.insert(root, arr[0])
        for i in range(1, len(arr)):
            max_result = max(max_result, self.findMaxXor(root, arr[i]))
            self.insert(root, arr[i])
        return max_result
        
        
if __name__ == "__main__":
    arr = [25, 10, 2, 8, 5, 3]
    print("Brute Force Approach to Maximum XOR in an array: ", maxXor_Brute(arr))
    
    print("Maxm XOR of 2 nos in an array using Bit Magic: ", maxXor_BitMagic(arr))
    obj = Solution()
    res = obj.maxXor(arr)
    print("Maximum XOR of two numbers in an array using Trie: ", res)
