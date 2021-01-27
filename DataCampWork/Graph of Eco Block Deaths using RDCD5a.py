import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')

data1 = pd.read_csv('RDCD5a.csv', index_col=0)
print(data1)
fig, ax = plt.subplots()
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
#Q1_Q3 = data["Jan":"Sep"]
ax.plot(data1.index, data1['BRICS'], label='BRICS')
ax.plot(data1.index, data1['EU'], label='EU')
ax.plot(data1.index, data1['US'], label='US')
ax.plot(data1.index, data1['All_Others'], label='All Others')
ax.set_xlabel('Q1-Q3 2020 (months)')
ax.set_ylabel("COVID Deaths Reported")
ax.set_title("COVID Related Deaths by select Economic Blocks")
ax.annotate('115k Deaths', xy=(3, 115000),  xycoords='data',
                xytext=(-100,-15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('57k Deaths', xy=(3, 57000),  xycoords='data',
                xytext=(-100,-15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('82k Deaths', xy=(8, 82000),  xycoords='data',
                xytext=(-0,-15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('72k Deaths', xy=(8, 72000),  xycoords='data',
                xytext=(0,-15), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.legend(loc=1)

plt.show()
fig.savefig('COVID Related Deaths by select Economic Blocks.png')
plt.close()