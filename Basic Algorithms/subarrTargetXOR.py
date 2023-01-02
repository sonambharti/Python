"""
A subarray is a contiguous part of array.
"""

#Brute-Force Approach

def subarrayTargetXOR(A, B):
    n = len(A)
    count = 0
    n = len(A)
    for i in range(n):
        s = 0
        for j in range(i,n):
            s = s^A[j]
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
