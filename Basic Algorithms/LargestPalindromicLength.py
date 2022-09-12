#Quesion asked in Amazon Interviews
#Find the length of largest possible palindromic string from a given string.
"""
Input:
str = "abccccdd"

Output:
7
"""

str = input()
s = set(str)
print(s)
res = []

for i in s:
    res.append(str.count(i))
    
print(res)
countLength = 0
for i in res:
    if i%2 == 0:
       countLength += i
       
       
print(sum+1)
