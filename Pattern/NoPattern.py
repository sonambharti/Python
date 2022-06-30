def f(n):
    # CODE HERE
    if n==0:
        return
    
    f(n-1)
    print([n]*n)
    

n = int(input())
f(n)
    
    

    
        
