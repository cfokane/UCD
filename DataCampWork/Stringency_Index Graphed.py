import matplotlib.pyplot as plt
#plt.style.use('seaborn-white')
import numpy as np
import pandas as pd


# Plot GDP/Year
data = pd.read_csv('RDCD9a.csv', index_col=0)
print(data)
fig, ax = plt.subplots()
#SI+4= Stringency_Indexed[>4]
#ax.plot(seventies.index, seventies["co2"])
Q1_Q3 = data["Jan":"Sep"]
ax.plot(Q1_Q3.index, Q1_Q3['Ireland'])
#ax.plot(Q1_Q3.index, Q1_Q3['EU'])
#ax.plot(Q1_Q3.index, Q1_Q3['US'])
#ax.plot(Q1_Q3.index, Q1_Q3['All_Others'])
ax.set_xlabel('Time (months)')
ax.set_ylabel("COVID Cases Reported")
ax.set_title("COVID Spread by Key Economic Blocks Q1-Q3 2020")


plt.show()