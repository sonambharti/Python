#Column wise plots

import numpy as np

import matplotlib.pyplot as plt

def f(t):

    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)

t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(221)
#no of plots, row wise or column wise(i.e. 1 for row wise and 2 for col-wise), where to place either 1st or 2 plot

plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(222)

plt.plot(t2, np.cos(2*np.pi*t2))

plt.show()