#Convert characters of a string to opposite case

str = input()
res = ""
for i in range(len(str)):
    if str[i].islower():
        res += str[i].upper()
        
    if str[i].isupper():
        res += (str[i].lower())
        
print(res)

"""
#2nd method

res = list(str)
for i in range(len(str)):
    if res[i]>='a' and res[i]<='z':
        res[i] = chr(ord(res[i])-32)
        
    elif res[i]>='A' and res[i]<='Z':
        res[i] = chr(ord(res[i])+32)
        
str = ''.join(res)
print(str)

"""
