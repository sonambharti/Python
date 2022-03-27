from matplotlib import pyplot as plt

x=[15,18,20]
y=[22,26,16]

x2=[16,19,21]
y2=[6,15,7]

plt.bar(x,y,color='r',label='Graph 1',width=.5) #(x-coordinate,y-coordinate,'color code for line',line-width)
plt.bar(x2,y2,color='g',label='Graph 2',width=.3)
plt.legend()  #legend() function is used to make labels of the line visible
plt.title('Graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid() #enable grid bydefault
plt.show()
