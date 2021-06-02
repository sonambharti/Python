""""
print:
*
**
***
****
*****

"""
num=int(input("Enter the no. of level you want to print for pattern: "))

for i in range(0,num):
    for j in range(0,i+1):
        print("*", end=' ')

    print()

""""
print:
1
1 2
1 2 3
1 2 3 4 

"""
num = int(input("Enter the no. of level you want to print for pattern: "))

for i in range(1, num):
    for j in range(1, i + 1):
        print(j, end=' ')

    print()