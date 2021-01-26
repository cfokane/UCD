import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import rcParams
data = pd.read_csv('RDCD9e.csv')
print(data)
#fig, ax =plt.subplots()
#ax.plot(data.index, data['Grand_Total'])
#ax.plot(data.index, data['Weekly_Deaths.161'])
#ax.set_xlabel("Week Number")
#ax.set_ylabel("Deaths vs Highest Stringency Level")
#ax.set_title('Implementation of Higher Stringency Levels')
#ax.annotate('Wk10 = 3 Countries', xy=(5, 2.5),  xycoords='data',
#                xytext=(1, 10), textcoords='offset points',
#                arrowprops=dict(arrowstyle="->")
#                )
#ax.annotate('Wk15 = 150 Countries', xy=(10, 150),  xycoords='data',
#                xytext=(-100, -20), textcoords='offset points',
#                arrowprops=dict(arrowstyle="->")
#                )
#ax.legend()
#plt.show()


#sns.regplot(x='All', y='All', data=data)
plt.show()