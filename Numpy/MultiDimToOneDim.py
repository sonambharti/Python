import numpy as np

#creating 1-d array with help of arange function of continous 6 values

a1 = np.arange(6)
print(a1)

a1 = a1.reshape(3,2)  # (rows,col)
print(a1)

print("size= ",a1.size)

print(a1)

print(a1.flatten())
