"""
A subarray is a contiguous part of array.
"""

#Brute-Force Approach

def subarrayTargetXOR(A, B):
    n = len(A)
    temp = []
    lst = []
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i,n+1):
            for k in range(i,j):
                temp.append(A[k])
            if temp:
                lst.append(temp)
            temp = []
                
    for i in range(len(lst)):
        arr = lst[i]
        s = 0
        for j in range(len(arr)):
            s = s^arr[j]
        if s == B:
            count += 1
       
    return count
    
    
A = []
n = int(input())
for i in range(n):
    ele = int(input())
    A.append(ele)
B = int(input())
ans = subarrayTargetXOR(A, B)
print(ans)
