#creating a numpy array and plot two graphs in a single line.

import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0,5,0.2) #creating a numpy array from range 0-5 with difference of 0.2
plt.plot(t,t,'r--',t,t**2,'bo') # (x1,y1,'1st-line-color with connector',x2,y2,'2nd-line-color with marker' )
plt.show()
