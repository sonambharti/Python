"""
Print the perfect number which lies between the given range.
Perfect Number: a perfect number is a positive integer that 
is equal to the sum of its positive divisors, excluding the 
number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself),
and 1 + 2 + 3 = 6, so 6 is a perfect number.
"""

def isPerfect(num):
    sum = 0
    for i in range(1, (num//2)+1):
        if num%i == 0:
            sum += i

    if sum == num:
        return True
        
    return False
    
def rangePerfect(num1, num2, res):
    for i in range(num1, num2+1):
        if isPerfect(i):
            res.append(i)
    

if __name__ == "__main__":
    num1 = int(input("Enter first input range: "))
    num2 = int(input("Enter second input range: "))
    
    res = []
    rangePerfect(num1, num2, res)
    #print(res)
    
    for i in res:
        print(i)
