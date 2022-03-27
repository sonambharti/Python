"""
Area plots are pretty much similar to the line plot.
They are also known as stack plots.
These plots can be used to track changes
over time for two or more related groups
that make up one whole category.
"""

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping =[7,8,6,11,7]

eating = [2,3,4,3,2]

working =[7,8,7,2,2]

playing = [8,5,7,8,13]

plt.plot([],[],color='m', label='Sleeping', linewidth=5)

plt.plot([],[],color='c', label='Eating', linewidth=5)

plt.plot([],[],color='r', label='Working', linewidth=5)

plt.plot([],[],color='k', label='Playing', linewidth=5)

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
# 'k' is for black
# 'm' is for dark pink
# c is for sky blue

plt.xlabel('x')

plt.ylabel('y')

plt.title('Stack Plot')

plt.legend()

plt.show()
