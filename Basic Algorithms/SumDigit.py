num = int(input("Enter any num: "))
pal = num
sum = 0
while (pal != 0):
    rem = pal % 10;
    sum = sum + rem
    pal = pal // 10

print("Sum = ", sum)