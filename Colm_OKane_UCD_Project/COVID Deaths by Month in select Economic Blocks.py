import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)
Econ_cases=(data.pivot_table(values='Weekly_Deaths', index=['Month'], columns=['Econ_Block'], aggfunc='sum', fill_value=0, margins=False))
# correct order of months
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
EconCases=Econ_cases.reindex(new_order, axis=0)


print(EconCases)
fig, ax = plt.subplots()
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
Q1_Q3 = EconCases["Jan":"Sep"]
ax.plot(Q1_Q3.index, Q1_Q3['BRICS'], label='BRICS')
ax.plot(Q1_Q3.index, Q1_Q3['EU'], label='EU')
ax.plot(Q1_Q3.index, Q1_Q3['US'], label='US')
ax.plot(Q1_Q3.index, Q1_Q3['All_Others'], label='All Others')
#plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 120000) #to set the axis ...xlim for x axis
plt.yticks([20000, 40000, 60000, 80000, 100000, 120000],['20k', '40k', '60k', '80k', '100k', '120k'])
ax.set_xlabel('Q1-Q3 2020 (Months)')
ax.set_ylabel("COVID Deaths Reported (Millions)")
ax.set_title("COVID Deaths by Month in select Economic Blocks")
ax.annotate('Wave 1 Cases Peak result in higher deaths in EU', xy=(3, 115000),  xycoords='data',
                xytext=(15, -20), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
ax.annotate('Death again', xy=(6, 1500000),  xycoords='data',
                xytext=(-50, 20), textcoords='offset points',
                 wrap=True)
ax.legend(loc=2)
plt.show()
fig.savefig('COVID Deaths by Month in select Economic Blocks.png')
plt.close()