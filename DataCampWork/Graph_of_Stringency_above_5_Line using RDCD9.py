import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams
plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCD9.csv', index_col=0)
print(data)
fig, ax =plt.subplots()
ax.plot(data['Grand_Total'], label='Stringency=5')
ax.set_xlabel("Week Number")
ax.set_ylabel("Number of Countries at Highest Stringency Level 5")
ax.set_title('Fig 9 Govt implementing Higher Restrictions in communities')
ax.annotate('Wk10 = 3 Countries', xy=(10, 2.5),  xycoords='data',
                xytext=(10, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('Wk15 = 150 Countries', xy=(15, 148),  xycoords='data',
                xytext=(10, -20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.legend()
plt.show()
fig.savefig('Stringency_Level5.png')
plt.close()
