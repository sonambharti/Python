#change color of the line

from matplotlib import pyplot as plt

x=[15,18,20]
y=[22,26,16]

plt.plot(x,y,'r',label='line',linewidth=2) #(x-coordinate,y-coordinate,'color code for line',line-width)