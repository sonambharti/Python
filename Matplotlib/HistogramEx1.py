"""
It shows distribution among data.

Difference between Histogram and bargraphs......
1. Bargraph is generally used for comparing different entites.
But, Histogram is used to show the distribution among data.
"""

from matplotlib import pyplot as plt

#age group---15-20,20-25,25-30

age = [2,5,3,5,5,4,4,2,2,5,5,4,18,12,16,21,19,24,18,17,17,21,24,27,19,17,15,19,24,22,23,19,25,26,27,30]
bins = [0,5,10,15,20,25,30,35]

plt.hist(age,bins,histtype='bar')

plt.show()
