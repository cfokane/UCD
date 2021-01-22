import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCD7.csv', index_col=0)
# newdf = df.loc[(df.origin == "JFK") | (df.origin == "LGA")] ...is the sort code
#data = data_.loc[(data_.Week_Numb >= 1) | (data_.Week_Numb <= 39)]
#print(data.head())
print(data.head())
#data1=(data1.sort_index(level=['Month'], ascending=[True])) #...would this sort months ascending?

from matplotlib import rcParams
rcParams['figure.figsize']=10,6 # to change size of graph
plt.plot(data.Weekly_Cases, color='m', linestyle='-')
plt.plot(data.Weekly_Deaths)
plt.legend(loc=2)
plt.grid(True, color='c', linestyle=':')
plt.xlabel('Week Number')
plt.ylim(0, 250000) #to set the axis ...xlim for x axis
plt.yticks((500000, 1000000, 1500000, 2000000, 2500000))
plt.ylabel('Cases')
plt.title('Global COVID Cases & Deaths Q1-Q3 2020')
plt.show() # or you could use plt.style.use('ggplot') or plt.style.use('fivethirtyeight')