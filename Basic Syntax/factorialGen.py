#find factorial using Generator
def factorial(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a

for x in factorial(5):
    print(x)
