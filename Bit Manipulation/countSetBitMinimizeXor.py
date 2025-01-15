'''
# 2429. Minimize XOR

Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.


Example 1:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example 2:
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
'''

def minimizeXor(num1, num2):
    def count_setBits(n):
        set_bits = 0
        while n:
            # each time we do and operation of n with (n-1) it will loose the LSB set-bit
            n = n & (n-1)
            set_bits += 1 # giving the count of set bit at the end
        return set_bits
    set_bits_num1 = count_setBits(num1)
    set_bits_num2 = count_setBits(num2)
    diff_set_bits = set_bits_num1 - set_bits_num2
    # diff_set_bits = num1.bit_count() - num2.bit_count()
    if diff_set_bits > 0:
        # Reset the 'diff_set_bits' least significant bits of the number 'num1'
        for _ in range(diff_set_bits):
            num1 &= num1 - 1
    else:
        # Set the 'diff_set_bits' least insignificant bits of the number 'num1'
        for _ in range(-diff_set_bits):
            num1 |= num1 + 1
    return num1
    
if __name__ == "__main__":
    num1 = 3
    num2 = 5
    print("The value of x to minimize XOR with num1, having equal no of set bits: ", minimizeXor(num1, num2))
