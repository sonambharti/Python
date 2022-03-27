from matplotlib import pyplot as plt

x = [2,2.5,3,3.5,4,4.5,5]
y = [7,6,8,5,10,10.5,11]

x1 = [4,5,7,8.6,9]
y1 = [6,3.3,4,3.8,6]

plt.plot(x,y,'ro-',label='line1') #here in'ro' o is called "marker". we can put any symbol instead.
plt.plot([3,4,5,6,7],[5,5.3,5.5,5.8,6],'g*',label='line2')
plt.plot(x1,y1,label='line3')
plt.title("Graph")
plt.xlabel("income")
plt.ylabel("savings")
plt.legend()

plt.show()
