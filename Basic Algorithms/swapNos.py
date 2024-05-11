"""
Write a program to swap 2 nos. using arthmetic operations
"""
def mulDivSwap(x, y):
    x = x * y
    y = x / y
    x = x / y
    return x, y
    
def addSubSwap(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y
    
if __name__ == "__main__":
    num1 = 2 
    num2 = 3
    print("num1 = ", num1, "num2 = ", num2)
    res1, res2 = mulDivSwap(num1, num2)
    print("num1 = ", res1, "num2 = ", res2)
    num3, num4 = 4, 5
    print("num3 = ", num3, "num4 = ", num4)
    res3, res4 = addSubSwap(num3, num4)
    print("num1 = ", res3, "num2 = ", res4)
