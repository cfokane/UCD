import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#plt.style.use('ggplot')
plt.style.use('seaborn-white')


data = pd.read_csv('RDCD4b.csv', index_col=0)
print(data)
fig, ax = plt.subplots()

#plt.figure(figsize=(6,4))
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
#plt.rcParams["figure.figsize"]=(200,60)

ax.plot(data.index, data['BRICS'], label='BRICS')
ax.plot(data.index, data['EU'], label='EU')
ax.plot(data.index, data['US'], label='US')
ax.plot(data.index, data['All_Others'], label='All Others')
#ax.plot(data.index, data['All'], label='All Countries')
ax.set_xlabel('2020 by Month')
ax.set_ylabel("Deaths as % of Monthly Cases by Block")
plt.ylim(0, 30) #to set the axis ...xlim for x axis
#plt.yticks([500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000],['0.5m', '1.0m', '1.5m', '2.0m', '2.5m', '3.0m', '3.5m', '4.0m', '4.5m'])

ax.set_title("Fig 4b COVID Deaths as % of Cases for selected Economic Blocks Q1-Q3 2020")

ax.annotate('Peak in Mortality Rate @ 23% Cases All Other Countries Cases', xy=(3, 23),  wrap=True, xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )

ax.legend(loc=2)

plt.show()
fig.savefig('Deaths as Proportion of Cases by Econ Blocks.png')
plt.close()