num = int(input("Enter any num: "))
pal = num
rev = 0
while(pal > 0):
    rem = pal%10;
    rev = (rev*10)+rem
    pal = pal//10 # here // is used for division arithmetic operation

print("reverse: ", rev)

if (num == rev):
    print(num," is a palindrome.")

else:
    print(num," is not a palindrome no.")
