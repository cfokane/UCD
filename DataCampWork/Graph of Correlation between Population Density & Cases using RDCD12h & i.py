import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import rcParams
#data1 = pd.read_csv('RDCD12g.csv')
#data1a=data1.sort_values('AreaKM2')
#print(data1a)
data2= pd.read_csv('RDCD12h.csv')
data2a=data2.sort_values('location')
print(data2a)
data3 = pd.read_csv('RDCD12i.csv')
data3a=data3.sort_values('location')
print(data3a)

fig, ax =plt.subplots()
plt.scatter(data3a['CasesxArea'], data2a['PopKM2'], s=data3a['CasesxArea']**3)
#plt.xscale('log')
plt.xlim(0, 12)
plt.ylim(0, 1500)
#lt.xticks([125000, 250000, 500000], rotation=45)
plt.xlabel('Cases per KM²')
plt.ylabel('Population Density (per KM²)')
plt.title('Fig (12h&i) Correlation between Population Density & Cases')
plt.xlim(0, 10) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 1500) #to set the axis ...xlim for x axis
plt.yticks([250, 500, 750, 1000, 1250, 1500],[ '250/KM²', '500/KM²', '750/KM²', '1000/KM²', '1250/KM²', '1500/KM²'])

plt.grid(True)
# Additional customizations
ax.annotate('Malta with 1397 people per KM²     recorded 9.6 cases per KM²', xy=(9.6, 1397),  xycoords='data',
                xytext=(-150, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True , color='red')
ax.annotate('Belgium with 380 people per KM² recorded           4.1 cases per KM²', xy=(4.1, 380),  xycoords='data',
                xytext=(-5, 48), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)
#plt.text(7, 1200, 'Malta with 1397 people per KM² recorded 9.6 cases per KM²', wrap=True)
#plt.text(4.1, 450, 'Belgium with 380 people per KM² recorded 4.1 cases per KM²', wrap=True)
plt.text(0.5, 15, 'Lower Cases per KM² where Population Density is lower')

plt.show()
fig.savefig('Correlation between Population Density & Cases.png')
plt.clf()