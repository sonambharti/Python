import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print("x= ",x)
print("y= ",y)

print("x+y = ",x + y)

print(np.add(x,y)) #adding 2 array index-wise using add function

print(x-y)

print(np.subtract(x,y))

print(x * y) #multiplying index-to-index wise

print(np.multiply(x,y)) #multiplying index-to-index wise

print(np.sqrt(x)) #sqrt to each elem of arr index wise

p = 9
print(np.sqrt(p))
