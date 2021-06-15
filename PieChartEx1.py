import matplotlib.pyplot as plt

days = [1,2,3,4,5]

slices = [2,2,2,13]

activities = ['sleeping','eating','working','playing']

cols = ['k','m','r','b']
# 'k' is for black
# 'm' is for dark pink
# c is for sky blue

plt.pie(slices,labels=activities,colors=cols,startangle=180  )

# pie(parts of graph, label for each part,colors of the part,start angle)

plt.title('Pie Plot')

plt.show()