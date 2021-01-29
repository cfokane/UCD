import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')

# Plot GDP/Year
data = pd.read_csv('RDCDFinal.csv', index_col=0)
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
plt.ylim(0, 50000) #to set the axis ...xlim for x axis
plt.yticks([5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000],['0.5k', '1.0k', '1.5k', '2.0k', '2.5k', '3.0k', '3.5k', '4.0k', '4.5k'])
ax.set_xlabel('Q1-Q3 2020 (Months)')
ax.set_ylabel("COVID Deaths Reported (Millions)")
ax.set_title("COVID Deaths by Month in select Economic Blocks")
ax.legend(loc=2)
plt.show()
fig.savefig('COVID Deaths by Month in select Economic Blocks.png')
plt.close()