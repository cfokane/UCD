import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCD8.csv', index_col=0)
#KCO3 = KCO2.loc[(KCO2.DATE >= '2020-01-30') & (KCO2.DATE <= '2020-02-30')] #not working
print(data)
print(data.head())
print(data.columns)
#data1=(data1.sort_index(level=['Month'], ascending=[True])) #...would this sort months ascending?

from matplotlib.pyplot import rcParams
rcParams['figure.figsize']=10,6 # to change size of graph
plt.plot(data.Grand_Total, color='m', linestyle='-')
#plt.plot(data.Week_Num)
plt.legend(loc=2)
plt.grid(True, color='c', linestyle=':')
plt.xlabel('Week Number')
plt.ylim(0, 250) #to set the axis ...xlim for x axis
plt.yticks((0, 50, 100, 150, 200, 250))
plt.ylabel('Number of Countries with Confirmed Cases')
plt.title('Speed of global spread COVID Cases & Deaths Q1-Q3 2020')
plt.show() # or you could use plt.style.use('ggplot') or plt.style.use('fivethirtyeight')