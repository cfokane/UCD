import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams

#Bubble Chart, cases per Area on YTD Wk39
data = pd.read_csv('RDCDFinal.csv', index_col=0)
#data2=[(data['location'] =='Ireland') & (data['location'] == 'United Kingdom')]     #boolean set to confirm Wednesday as True
data['British_Isles'] = data['location'].isin(['Ireland', 'United Kingdom'])
data2=data.query('British_Isles == True')
print(data2.columns)
PopDen=(data2.pivot_table(values=['Deaths_%_Cases', 'Week_Num', 'PopMi2'], index='location', aggfunc='sum', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
PopDen.to_csv('PopDen2.csv')
#CaseArea=(data2.pivot_table(values=['Cases_x_Area'], index='location', aggfunc='sum', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
#CaseArea.to_csv('CaseArea2.csv')
#print(CaseArea)

fig, ax = plt.subplots(figsize=(12,6))
plt.scatter(PopDen['PopMi2'], PopDen['Week_Num'], s=PopDen['Deaths_%_Cases'])
plt.xlabel('PopMi2')
plt.ylabel('Week_Num')
plt.title('Correlation between Population Density & Stuff')
#plt.xlim(0, 5000) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#plt.yscale('log')
#plt.ylim(0, 25000) #to set the axis ...xlim for x axis


#plt.yticks([50, 250, 500, 1000, 2500, 5000, 10000, 20000],['50/Mi²','250/Mi²', '500/Mi²', '1000/Mi²', '2500/Mi²', '5000/Mi²', '10000/Mi²', '20000/Mi²'])

plt.grid(True)
# Additional customizations
ax.annotate('Monaco recorded 107 cases per Mi²', xy=(107, 20000),  xycoords='data',
                xytext=(-10, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True, color='red')
ax.annotate('Bahrain 106 cse/Mi²', xy=(106, 2600),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )
ax.annotate('Singapore 83 cse/Mi²', xy=(83, 8400),  xycoords='data',
                xytext=(-15, -50), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True )

plt.text(3, 80, '} Lower Cases per Mi² where Population Density is lower')

plt.show()
fig.savefig('Correlation between Population Density & Cases UK&I.png')
plt.close()