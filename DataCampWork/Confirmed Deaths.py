import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('RDCD8a.csv', index_col=0)
print(data)
from matplotlib.pyplot import rcParams
fig, ax =plt.subplots()
rcParams['figure.figsize']=10,15 # to change size of graph
plt.plot(data.Grand_Total_Deaths, color='m', marker='o', linestyle='-', label='Deaths Recorded')
#plt.plot(data.Week_Num)
plt.grid(True, color='g',linestyle=':')
plt.xlabel('Week Number')
plt.ylim(0, 60000) #to set the axis ...xlim for x axis
plt.yticks((0, 10000, 20000, 30000, 40000, 50000, 60000))
plt.ylabel('Number of Confirmed Deaths')
plt.title('Fig 8a: Global mortality COVID: Deaths recorded Q1-Q3 2020')
plt.legend(loc=2)
ax.annotate('Wk15 = Wave1 Peak Deaths', xy=(16, 52000),  xycoords='data',
                xytext=(15, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
#ax.legend()
plt.show() ; # or you could use plt.style.use('ggplot') or plt.style.use('fivethirtyeight')
plt.clf()