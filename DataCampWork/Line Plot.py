import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCD1.csv',index_col=16)
print(data.head())
print(data.columns)


from matplotlib import rcParams
rcParams['figure.figsize']=10,6 # to change size of graph
plt.plot(data.Weekly_Cases, color='m', linestyle=':')
plt.plot(data.Weekly_Deaths)
plt.legend(loc=2)
plt.grid(True, color='c', linestyle=':')
plt.xlabel('Cases')
plt.ylim(1000, 10000) #to set the axis ...xlim for x axis
plt.yticks((1000, 5000, 7500))
plt.ylabel('Time')
plt.title('COVID Cases & Deaths Q1-Q3 2020')
plt.show() # or you could use plt.style.use('ggplot') or plt.style.use('fivethirtyeight')