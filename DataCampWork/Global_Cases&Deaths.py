import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCD7.csv', index_col=0)
fig, ax = plt.subplots()
ax.plot(data.index, data['Weekly_Cases'], color='b')
ax.set_xlabel('Week Number')
ax.set_ylabel('Cases', color='b')
ax.tick_params('y', colors='blue')
ax2 = ax.twinx()
ax2.plot(data.index, data['Weekly_Deaths'], color='red')
ax2.set_ylabel('Deaths', color='red')
ax2.tick_params('y', colors='red')
ax2.annotate('X Countries record cases of CoVid19', xy=(pd.Timestamp('2020-03-01'), 1), xytext=(pd.Timestamp('2020-03-15'), 0.2), arrowprops={'arrowstyle':'->', 'color':'grey'})
plt.show()
#, colour='red'