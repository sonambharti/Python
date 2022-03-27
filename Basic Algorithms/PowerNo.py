#WAP to find numbers which are in between integer to
# and integer n and such that the sum of its digit raised to 
#the third power is equal to the number

n = int(input("Enter the input: "))
x=[]
if(n>10000):
    print("Wrong Input")
else:
    for i in range(2,n+1):
        s=0
        t=i
        while t>0:
            d=t%10
            s+=(d**3)
            t//=10
        if s==i:
            x.append(i)
    if len(x)==0:
        print("No Number found")
    else:
        for i in x:
            print(i,end=" ")
