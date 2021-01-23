import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import numpy as np
import pandas as pd
from numpy import array

# Plot GDP/Year
data = pd.read_csv('RDCD6a.csv', index_col=0)
print(data)
fig, ax = plt.subplots()
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
Q1_Q3 = data["Jan":"Sep"]
ax.plot(Q1_Q3.index, Q1_Q3['BRICS'])
ax.plot(Q1_Q3.index, Q1_Q3['EU'])
ax.plot(Q1_Q3.index, Q1_Q3['US'])
ax.plot(Q1_Q3.index, Q1_Q3['All_Others'])

plt.show()