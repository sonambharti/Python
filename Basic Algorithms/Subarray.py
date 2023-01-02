
"""
A subarray is a contiguous part of array.
"""

#Brute-Force Approach

def subarray(A):
    n = len(A)    
    temp = []
    lst = []
    for i in range(n):
        for j in range(i,n+1):
            for k in range(i,j):
                temp.append(A[k])
            if temp:
                lst.append(temp)
            temp = []
    return lst
    
    
A = []
n = int(input())
for i in range(n):
    ele = int(input())
    A.append(ele)

ans = subarray(A)
print(ans)
