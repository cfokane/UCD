import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCD1.csv') #,index_col=15
#print(data.head())
print(data.columns)

# Long Way(data.location == "Ireland")
newdata = data.loc[(data.Econ_Block == "EU")]
newdata2 = newdata.loc[(newdata.day == "Wednesday")]
newdata3 = newdata2.loc[(newdata2.location == "Ireland")]


print(newdata3)
# Smart Way
#newdf = df[df.origin.isin(["JFK", "LGA"])]


from matplotlib import rcParams
rcParams['figure.figsize']=10,6 # to change size of graph
plt.plot(newdata4.Weekly_Cases, color='m', linestyle='-')
plt.plot(newdata4.Weekly_Deaths)
plt.legend(loc=2)
plt.grid(True, color='c', linestyle=':')
plt.xlabel('Week Number')
#plt.ylim(0, 1000) #to set the axis ...xlim for x axis
plt.yticks((100, 500, 750))
plt.ylabel('Cases')
plt.title('Irish COVID Cases & Deaths Q1-Q3 2020')
plt.show() # or you could use plt.style.use('ggplot') or plt.style.use('fivethirtyeight')