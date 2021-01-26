import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import rcParams

#we want 'Total_Cases' & 'Pop_Density
#
# data1 = pd.read_csv('RDCD12g.csv', index_col=0)
# data1a=data1.sort_values('AreaKM2')
# print(data1a)

data3 = pd.read_csv('RDCD12l.csv', index_col=0)
# data3a=data3.sort_values('CasesxArea')
print(data3)

data3.plot(x='Population Density', y='total_cases', kind= 'scatter', s=data3['CasesxArea']**3)
plt.xlabel('Population Density')
plt.ylabel('total_cases')
plt.title('Fig 12ghi Correlation between Population Density & Cases')
plt.grid(True)
# Additional customizations
plt.text(1200, 7, 'Malta 1397 people per KM2 recorded 9.6 cases per KM2')
plt.text(200,800 , 'Spain 92 people per KM2 recorded 4.1 cases per KM2')
#plt.text(0.5, 15, 'Finland 16 people per KM2 recorded 0.03 cases per KM2')
plt.show()
plt.clf()