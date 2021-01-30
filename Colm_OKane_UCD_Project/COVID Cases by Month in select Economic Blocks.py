import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)
Econ_cases=(data.pivot_table(values='Weekly_Cases', index=['Month'], columns=['Econ_Block'], aggfunc='sum', fill_value=0, margins=False))
# correct order of months
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
EconCases=Econ_cases.reindex(new_order, axis=0)


print(EconCases)
fig, ax = plt.subplots(figsize=(12,5))
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
Q1_Q3 = EconCases["Jan":"Sep"]
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
ax.set_title("COVID Cases by Month in select Economic Blocks")
ax.annotate('Wave1 Peak', xy=(3, 1000000),  xycoords='data',
                xytext=(-15, 20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Following weeks of stability, weekly case rates accelerate again', xy=(4.2, 2000000),  xycoords='data',
                xytext=(-50, 20), textcoords='offset points', wrap=True)
ax.legend(loc=2)
plt.show()
fig.savefig('COVID Cases by Month in select Economic Blocks.png')
plt.close()