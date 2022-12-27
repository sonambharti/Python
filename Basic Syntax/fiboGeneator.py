#Python program to generate a fibonaci series using generator

def fibo(n):
    a = 0
    b = 1
    for i in range(n-1):
        yield a
        a, b = b, a+b 
        
for i in fibo(11):
    print(i)
