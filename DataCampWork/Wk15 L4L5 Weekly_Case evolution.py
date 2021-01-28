import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams


RDCDS = pd.read_csv('RDCD2.csv')
# filter columns to isolate countries who had higher stringency levels in Wk15
RDCDSQ=RDCDS.query('Stringency_Indexed >=4')
RDCDSQ.loc[:, 'Stringency_Indexed_Wk15']= RDCDSQ['Week_Num']==15
RDCDSQ1=RDCDSQ.query('Stringency_Indexed_Wk15 ==True')
print(RDCDSQ1.columns)
del RDCDSQ1['Unnamed: 0']
del RDCDSQ1['Unnamed: 0.1']
del RDCDSQ1['location']
del RDCDSQ1['date']
del RDCDSQ1['total_cases']
del RDCDSQ1['total_deaths']
del RDCDSQ1['stringency_index']
del RDCDSQ1['population']
del RDCDSQ1['gdp_per_capita']
del RDCDSQ1['human_development_index']
del RDCDSQ1['DATE_RD']
del RDCDSQ1['DATE_CD']
del RDCDSQ1['Country_x']
del RDCDSQ1['European Union']
del RDCDSQ1['Area (km²)']
del RDCDSQ1['Population Density']
del RDCDSQ1['DATE']
del RDCDSQ1['Week_Num']
del RDCDSQ1['Month']
del RDCDSQ1['day']
del RDCDSQ1['dayz']
del RDCDSQ1['Dates']
del RDCDSQ1['Wednesdays']
del RDCDSQ1['CasesxArea']
del RDCDSQ1['CasesxPop']
del RDCDSQ1['DeathsxCases']
del RDCDSQ1['AreaKM2']
del RDCDSQ1['PopKM2']
del RDCDSQ1['Stringency_Indexed']
del RDCDSQ1['Econ_Block']
del RDCDSQ1['Weekly_Cases']
del RDCDSQ1['Weekly_Deaths']
del RDCDSQ1['Stringency_Index_5']

#output this to csv
RDCDSQ1.to_csv('RDCDSQ1.csv')
RDCDSQ1 = pd.read_csv('RDCDSQ1.csv')
RDCD2 = pd.read_csv('RDCD11.csv')
print(RDCD2.columns)
# Merge countries who had higher stringency levels in Wk15 dataset to add filterable column RDCD dataset
RDCDSTRHIGH = (RDCD2.merge(RDCDSQ1, on='iso_code', how='left'))
print(RDCDSTRHIGH.isna().sum())
#could fill new column blanks...lets see
print(RDCDSTRHIGH.columns)
RDCDSTRHIGH.to_csv('RDCDSTRHIGH.csv')
data = pd.read_csv('RDCDSTRHIGH.csv')
fig, ax = plt.subplots()
data = data.convert_objects(convert_numeric=True)
sub_df = data.groupby(['RECL_LCC','RECL_PI'])['COUNT'].sum().unstack()
sub_df.plot(kind='bar',stacked=True)
#ax.stackplot(data['population'], data['Stringency_Indexed'].values(),
#             labels=data['Stringency_Indexed'].keys())
#ax.legend(loc='upper left')
#ax.set_title('World population')
#ax.set_xlabel('Year')
#ax.set_ylabel('Number of people (millions)')

plt.show()

#RDCDSTRHIGHTrue=RDCDSTRHIGH.query('Stringency_Indexed_Wk15 ==True')
#print(RDCDSTRHIGHTrue)
#fig, ax = plt.subplots()
#plt.style.use('seaborn-whitegrid')
#ax.stackplot('population', 'Stringency_Indexed')
#plt.show()
#ax.plot(RDCDSTRHIGHTrue.index, RDCDSTRHIGHTrue['Stringency_Indexed'], color='b', label='Cases Recorded Globally per Week')
#ax.set_ylabel('Stringency Indexed', color='b')
#ax.tick_params('y', colors='blue')
#plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#plt.ylim(0, 2500000) #to set the axis ...xlim for x axis
#plt.yticks([500000, 1000000, 1500000, 2000000, 2500000],['0.5m', '1.0m', '1.5m', '2.0m', '2.5m'])
#ax2 = ax.twinx()
#ax2.plot(RDCDSTRHIGHTrue.index, RDCDSTRHIGHTrue['Stringency_Indexed'], color='red', label='Global Deaths as % of Cases')
#ax2.set_ylabel('Stringency_Indexed_Wk15', color='red')
#ax2.tick_params('y', colors='red')
#ax.set_title('xxx')
#ax2.annotate('xx', xy=(18, 7.2),  xycoords='data',
#                xytext=(-35, -80), textcoords='offset points',
#                arrowprops=dict(arrowstyle="->"))

#ax.annotate('x', xy=(23, 800000),  xycoords='data',
#                xytext=(-0, -40), textcoords='offset points',
#                arrowprops=dict(arrowstyle="->"))

#plt.legend()
#plt.show()
#fig.savefig('RDCDSTRHIGH.png')
#plt.close()




