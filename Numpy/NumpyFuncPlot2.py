# creating a numpy array and plot multiple graphs in a single line.

import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0, 5, 0.2)  # creating a numpy array from range 0-5 with difference of 0.2

plt.plot(t, t * 2, 'r--', t, t ** 2, 'bo', t * 2, t * 1.5, 'g*-')  # no labels can be included

plt.title("Multi Graph")
plt.xlabel("Cost")
plt.ylabel("Expenditure")
plt.grid()
plt.show()