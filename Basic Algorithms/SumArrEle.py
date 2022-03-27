import numpy as np

a = np.array([[1,2,3],[10,20,30]])
print(a)

print("Sum= ",a.sum())  #sum all the array elements

print("Col-wise sum= ",np.sum(a,axis=0)) #column-wise sum

print("Row-wise sum= ",np.sum(a,axis=1)) #row-wise sum
