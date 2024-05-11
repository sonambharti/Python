"""
Write a program to swap 2 nos. using xor bitwise operation
"""

def bitSwap(num1, num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2

    return [num1, num2]
    
if __name__ == "__main__":
    num1 = 2 
    num2 = 3
    print("num1 = ", num1, "num2 = ", num2)
    res = bitSwap(num1, num2)
    print("num1 = ", res[0], "num2 = ", res[1])
