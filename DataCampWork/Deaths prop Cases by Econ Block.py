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

ax.plot(data.index, data['BRICS'])
ax.plot(data.index, data['EU'])
ax.plot(data.index, data['US'])
ax.plot(data.index, data['All_Others'])
ax.plot(data.index, data['All'])
ax.set_xlabel('Time (months)')
ax.set_ylabel("Cases as Proportion of Deaths")
ax.set_title("COVID Deaths as Prop of Cases across Key Economic Blocks Q1-Q3 2020")


plt.show()