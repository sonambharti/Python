#creating a numpy array and plot a graph.

import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0,5,0.2) #creating a numpy array from range 0-5 with difference of 0.2
plt.plot(t,t,'r--') # here '--' is line-connector btwn two points of a graph
plt.show()
