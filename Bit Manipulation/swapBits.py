"""
Given an unsigned integer N. The task is to swap all odd bits with even bits. 
For example, if the given number is 23 (00010111), it should be converted to 43(00101011). 
Here, every even position bit is swapped with an adjacent bit on the right side(even 
position bits are highlighted in the binary representation of 23), and every odd position 
bit is swapped with an adjacent on the left side.

Example 1:

Input: N = 23
Output: 43
Explanation: 
Binary representation of the given number 
is 00010111 after swapping 
00101011 = 43 in decimal.
"""

def swapBits(n):
    # Mask for even bits (101010...)
    even_mask = 0xAAAAAAAA
    # Mask for odd bits (010101...)
    odd_mask = 0x55555555
    
    # Right shift even bits and left shift odd bits
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    
    # Combine even and odd bits using bitwise OR
    return even_bits | odd_bits

if __name__ == "__main__":
  # Example usage
  N = 23
  print("Output:", swapBits(N))
