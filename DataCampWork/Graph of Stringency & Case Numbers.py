import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams

#Graph Stringency & Cases on two y axes

data = pd.read_csv('StringL5WkTot.csv', index_col=0)

print(data)
fig, ax =plt.subplots()
ax.plot(data['All'], label='Stringency=5 (Scale=1-5)')
ax.set_xlabel("Week Number")
ax.set_ylabel("Number of Countries at Highest Stringency Level")
ax.set_title('Impact on COIVD case numbers at higher Stringency Levels')
#ax2 = ax.twinx()
#ax2.plot(data.index, data['DeathsxCases'], color='red', label='Global Deaths as % of Cases')
#ax2.set_ylabel('Deaths', color='red')
#ax2.tick_params('y', colors='red')


ax.annotate('Wk10 = 3 Countries', xy=(5, 2.5),  xycoords='data',
                xytext=(1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('Wk15 = 150 Countries', xy=(10, 150),  xycoords='data',
                xytext=(-100, -20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )

ax.legend()
plt.show()
plt.clf()



#fig, ax =plt.subplots()
#data.iloc[38].hist(bins=bins)
#ax.hist(data['location'], label='Level 5')
#ax.hist(data['Grand_Total'], label='Stringency', bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39])
#ax.set_xlabel("Stringency 4&5")

#ax.legend
#ax.set_title("")
#plt.show()