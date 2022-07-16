def gcd(m,n):
    if(m==0 or n==0 or m==n):
        if(m==0):
            return n
        if(n==0):
            return m
        if(m == n):
            return n
            
    else:
            
        if(m>n):
            res = gcd(m%n, n)
                
        else:
            res = gcd(m, n%m)
                
    return res
    
    
m = int(input("Enter 1st number: "))
n = int(input("Enter 2nd number: "))

res = gcd(m,n)
print(res)
