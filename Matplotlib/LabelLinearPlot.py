# make label of line to visible

from matplotlib import pyplot as plt

x=[15,18,20]
y=[22,26,16]

x2=[6,9,11]
y2=[6,15,7]

plt.plot(x,y,'r',label='line 1',linewidth=2) #(x-coordinate,y-coordinate,'color code for line',line-width)
plt.plot(x2,y2,'g',label='line2',linewidth=4)
plt.legend()  # legend() function is used to make labels of the line visible

plt.show()
