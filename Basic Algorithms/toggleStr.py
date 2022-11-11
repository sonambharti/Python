#Convert characters of a string to opposite case

str = input()
res = ""
for i in range(len(str)):
    if str[i].islower():
        res += str[i].upper()
        
    if str[i].isupper():
        res += (str[i].lower())
        
print(res)
