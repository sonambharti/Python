num = int(input("Enter a number:"))

for i in range(2,num//2):
    while(num%i == 0):
        print(i," ",end="")
        num = num//i

if (num>2):
    print(num)