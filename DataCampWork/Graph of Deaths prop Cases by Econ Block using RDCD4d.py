import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np
import pandas as pd


# Plot GDP/Year
data = pd.read_csv('RDCD4b.csv', index_col=0)
print(data)
fig, ax = plt.subplots()
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
#rcParams['figure.figsize']=10,6
ax.plot(data.index, data['BRICS'], label='BRICS')
ax.plot(data.index, data['EU'], label='EU')
ax.plot(data.index, data['US'], label='US')
ax.plot(data.index, data['All_Others'], label='All Others')
#ax.plot(data.index, data['All'], label='All Countries')
ax.set_xlabel('2020 (Months)')
ax.set_ylabel("Deaths as Proportion of Cases")
ax.set_title("Fig 4b COVID Deaths as Prop of Cases across Key Economic Blocks Q1-Q3 2020")

ax.annotate('April saw Peak in cases in All Other Countries', xy=(3, 23),  xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )

ax.legend()

plt.show()