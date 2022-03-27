# 3-d Plot
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#Here we need to import data file

iris = pd.read_csv('Iris.csv') # read_csv('name of the required file')

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

for species,irisubset in iris.groupby('Species'):
  ax.scatter(irisubset['PetalLengthCm'],irisubset['PetalWidthCm'],irisubset['SepalLengthCm'],label=species)

plt.legend()

ax.set_xlabel('PetalLength')
ax.set_ylabel('PetalWidth')
ax.set_zlabel('SepalLength')
plt.show()
