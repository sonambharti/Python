# first we will plot 2-d graph btw 2 data parameter

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Here we need to import data file

iris = pd.read_csv('Iris.csv') #read_csv('name of the required file')
print(iris)

for species,irisubset in iris.groupby('Species'):
  plt.scatter(irisubset['PetalLengthCm'],irisubset['PetalWidthCm'],label=species)
#here 'isisubset' means we are taking subset from iris
plt.legend()
plt.show()