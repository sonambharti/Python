"""
#   191. Number of 1 Bits

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits 
it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given 
as a signed integer type. It should not affect your implementation, as the integer's internal binary representation 
is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input 
represents the signed integer. -3.
 

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.

Example 3:
Input: n = 128
Output: 1
Explanation: The input binary string 10000000 has a total of one set bit.

"""
# def hammingWeight(n):
#         count = 0
#         while n != 0:
#             count += (n%2)
#             n >>= 1
#         return count

# def hammingWeights(n):
#     count = 0
#     binary = bin(n)
#     for b in binary:
#         if b == '1':
#             count += 1
#     return count

def hammingWeights(n):
    count = 0
    binary = ""
    while n != 0:
        count += (n%2)
        n //= 2
    return count

n = 3
res = hammingWeight(n)
print("No. of n = ", res)
