import numpy as np

a = np.array([[1,2,3],[10,20,30]])

print("Given array:\n",a)

print(a.reshape(3,2)) #here we changed the dimension of array

print(a.reshape(2,3))

print(a.reshape(1,6))

print(a.reshape(6,1))