'''
# Maximize your health

You are given two types of drinks A and B which can boost your health. There are 
n drink glasses of each type arranged in seperate lines. You can drink atmost x 
glasses of drink A and atmost y glasses of drink B to maximize your health, but 
there are some conditions that must be followed -

1. You have to drink the glasses from left to right from each row.
2. If you started to drink of B type glassesthen you can't drink A type glasses.
3. On each index i, you can choose drink A glass (A[i], if any B type glass hasn't 
   been choosen yet)
   or drink B glass (B[i] or non of these and your health update accordingly. 
   (1-base) indexing is used).
   
   
Note: Your initial health is 0.

Examples :

Input: n = 5
    A = [5, -1, -3, -2, 1]
    B = [-2, 1, 5, 4, 2]
    x = 2
    y = 2
Output: 14

'''


from typing import List
from heapq import *
from collections import deque


def maximizeHealth(n, A, B, x, y):
    # code here
    pq = []
    pa = [0 for _ in range(n+1)]
    summ = 0
    
    for i in range(n):
        if (A[i] >= 0):
            heappush(pq, A[i])
            summ += A[i]
            if len(pq) > x:
                el = heappop(pq)
                summ -= el
                # heappop(pq)
        
        pa[i+1] = summ
    
    while len(pq) > 0:
        pq.pop()
    # pq.clear()
    
    summ = 0
    mx = pa[n]
    
    for i in range(n-1, -1, -1):
        if (B[i] >= 0):
            heappush(pq, B[i])
            summ += B[i]
            if len(pq) > y:
                el = heappop(pq)
                summ -= el
                # heappop(pq)
        mx = max(mx, (pa[i] + summ))
    
    return mx
    
    
if __name__ == "__main__":
    n = 5
    A = [5, -1, -3, -2, 1]
    B = [-2, 1, 5, 4, 2]
    x, y = 2, 2
    
    res = maximizeHealth(n, A, B, x, y)
    print("Result = ", res)
