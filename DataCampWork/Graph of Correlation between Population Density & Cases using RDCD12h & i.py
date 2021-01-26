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

plt.scatter(data3a['CasesxArea'], data2a['PopKM2'], s=data3a['CasesxArea']**3)
#plt.xscale('log')
plt.xlim(0, 12)
plt.ylim(0, 1500)
#lt.xticks([125000, 250000, 500000], rotation=45)
plt.xlabel('Cases per KM²')
plt.ylabel('Population per KM²')
plt.title('Fig 12ghi Correlation between Population Density & Cases')
plt.grid(True)
# Additional customizations
plt.text(7, 1200, 'Malta 1397 people per KM² recorded 9.6 cases per KM²')
plt.text(4.1, 450, 'Belgium 380 people per KM² recorded 4.1 cases per KM²')
plt.text(0.5, 15, 'Lower Cases per KM² where Population Density is lower')
plt.show()
plt.clf()