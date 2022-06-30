def f(n):
    # CODE HERE
    if n==0:
        return
    print([n]*n)
    f(n-1)
    
n = int(input())
f(n)
