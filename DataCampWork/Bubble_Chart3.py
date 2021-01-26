import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import rcParams
data1 = pd.read_csv('RDCD12g.csv', index_col=0)
data1a=data1.sort_values('AreaKM2')
print(data1a)
data2= pd.read_csv('RDCD12k.csv', index_col=0)
data2a=data2.sort_values('Population Density')
print(data2a)
data3 = pd.read_csv('RDCD12i.csv', index_col=0)
data3a=data3.sort_values('CasesxArea')
print(data3)

plt.scatter(data1['AreaKM2'], data3a['CasesxArea'],s=data3a['CasesxArea']**2)
#plt.xscale('log')
#plt.xlim(0, 12)
#plt.ylim(0, 1500)
#lt.xticks([125000, 250000, 500000], rotation=45)
plt.xlabel('AreaKM2')
plt.ylabel('Population Density')
plt.title('Fig 12ghi Correlation between Population Density & Cases')
plt.grid(True)
# Additional customizations
#plt.text(9.6, 316, 'Malta')
#plt.text(4.1, 30500, 'Belgium')
#plt.text(0.5, 15, 'Finland 16 people per KM2 recorded 0.03 cases per KM2')
plt.show()
plt.clf()