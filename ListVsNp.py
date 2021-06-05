import numpy as np
import time
import sys

l1 = [1,2,3]
l2 = [9,8,7]

s1 = l1 + l2

print("L1+L2 = ",s1)

size = 10000
l1=range(size)
l2=range(size)

n1 = np.arange(size)
n2 = np.arange(size)

#list item-wise sum
start = time.time() #from time module pick time func
res = [(x+y) for x,y in zip(l1,l2)]
print((time.time()-start)*1000)

#numpy array itemwise sum
start = time.time()
res1 = n1+n2
print((time.time()-start)*1000)