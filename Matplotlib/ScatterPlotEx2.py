#multiple scatter graph

from matplotlib import pyplot as plt
x = [2,2.5,3,3.5,4,4.5,5]
y = [8,8.5,9,9.5,10,10.5,11]

x1 = [3,4,7,8,9]
y1 = [3,6,8,9.8,11.5]

plt.scatter(x,y,color='r',label='line1')
plt.scatter(x1,y1,color='g',label='line2')
plt.title("Scatter Plot")
plt.xlabel("income")
plt.ylabel("savings")
plt.legend()

plt.show()
