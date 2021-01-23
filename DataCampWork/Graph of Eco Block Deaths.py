import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np
import pandas as pd


# Plot GDP/Year
data1 = pd.read_csv('RDCD5a.csv', index_col=0)
print(data1)
fig, ax = plt.subplots()
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
#Q1_Q3 = data["Jan":"Sep"]
ax.plot(data1.index, data1['BRICS'])
ax.plot(data1.index, data1['EU'])
ax.plot(data1.index, data1['US'])
ax.plot(data1.index, data1['All_Others'])
ax.set_xlabel('Time (months)')
ax.set_ylabel("COVID Deaths Reported")
ax.set_title("COVID Related Deaths by Key Economic Blocks Q1-Q3 2020")


plt.show()