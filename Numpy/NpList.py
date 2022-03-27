# Numpy array is fast.
# NumPy takes less memory
# NumPy is more convinient to use.
# NumPy is used for larger scientific calculation.

import numpy as np

import sys

list = range(1000)

# sys module calculate size(in byte) in python
a = 10
print(sys.getsizeof(a)) #memory located to a
print(sys.getsizeof(a)*len(list))

a1 = np.arange(1000)
print(a1.size*a1.itemsize)
