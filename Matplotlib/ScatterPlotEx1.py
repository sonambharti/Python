from matplotlib import pyplot as plt
x = [2,2.5,3,3.5,4,4.5,5]
y = [8,8.5,9,9.5,10,10.5,11]

plt.scatter(x,y,color='r',label='line1')
plt.title("Scatter Plot")
plt.xlabel("income")
plt.ylabel("savings")
plt.legend()

plt.show()

plt.plot()
