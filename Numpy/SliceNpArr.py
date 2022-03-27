import numpy as np

a = np.array([[1,2,3],[10,20,30]])
print(a)

print(a[0,0])

print(a[0,1])

print(a[0:,1]) #(row,column) slice row and col individually

print(a[1:,1:2])

print(a[1:,:2])

print(a[1:,1:])