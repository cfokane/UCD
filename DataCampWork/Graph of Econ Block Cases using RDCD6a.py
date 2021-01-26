import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np
import pandas as pd


# Plot GDP/Year
data = pd.read_csv('RDCD6a.csv', index_col=0)
print(data)
fig, ax = plt.subplots()
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
Q1_Q3 = data["Jan":"Sep"]
ax.plot(Q1_Q3.index, Q1_Q3['BRICS'], label='BRICS')
ax.plot(Q1_Q3.index, Q1_Q3['EU'], label='EU')
ax.plot(Q1_Q3.index, Q1_Q3['US'], label='US')
ax.plot(Q1_Q3.index, Q1_Q3['All_Others'], label='All Others')
#plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 4500000) #to set the axis ...xlim for x axis
plt.yticks([500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000],['0.5m', '1.0m', '1.5m', '2.0m', '2.5m', '3.0m', '3.5m', '4.0m', '4.5m'])
ax.set_xlabel('Q1-Q3 2020 (Months)')
ax.set_ylabel("COVID Cases Reported (Millions)")
ax.set_title("COVID Cases by Month in Key Economic Blocks")
ax.legend()

plt.show()
fig.savefig('COVID Cases by Month in Key Economic Blocks.png')
