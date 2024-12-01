'''
# Max X

Given a positive integer n, find the maximum integer x such that 2^x <= n.

Examples:
    
    Input: n = 17
    Output: 4
    
    Input: 8
    Output: 3
    
'''


import math


def findMaxX(n):
    # code here
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    return math.floor(math.log2(n))
    
    
if __name__ == "__main__":
    n = 17
    print("Maximum value of x = ", findMaxX(n))

