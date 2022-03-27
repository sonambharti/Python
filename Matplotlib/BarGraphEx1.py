# Example of bar graph
#Used in measuring the changes between two quantity.

from matplotlib import pyplot as plt

plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
        label='BMW', color='r',width=.1)


plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,70,50,60],
        label='Audi', color='b',width=.2)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance(in kms.')
plt.title('Information')

plt.show()