import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#plt.style.use('ggplot')
plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv')
RD=data.query('location == "United Kingdom"')
print(RD.columns)


RD=(RD.pivot_table(values=['Deaths_%_Cases', 'Stringency_Indexed'] , index='Week_Num', columns='location', aggfunc='sum',fill_value=0, margins=False).iloc[:-1,:])
#new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
#RD1=RD.reindex(new_order, axis=0)
print(RD.columns)



#RD2 = RD1.loc[:, ['Deaths_%_Cases','Stringency_Indexed', 'Month', 'location']]
#print(RD2)

fig, ax1 = plt.subplots(figsize=(12,5))
plt.style.use('seaborn-whitegrid')

ax1.set_xlabel('Weeks')
ax1 .plot(RD.index, RD['Deaths_%_Cases'], color='b', label='Deaths_%_Cases')
ax1.set_ylabel('Deaths_%_Cases', color='b')
ax1.tick_params(axis='y', colors='blue')

#plt.xlim(, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 20) #to set the axis ...xlim for x axis
plt.yticks([5, 10, 15, 20,],['5%', '10%', '15%', '20%'])
ax2 = ax1.twinx()
color='tab:red'
ax2.plot(RD.index, RD['Stringency_Indexed'], color='red', label='Stringency_Indexed')
ax2.set_ylabel('Stringency_Indexed', color='red')
ax2.tick_params('y', colors='red')
ax1.set_title('Deaths as a % of Cases & Stringency Levels UK')
ax2.annotate('Over 7 in 100 people with disease are dying', xy=(18, 7.2),  xycoords='data',
                xytext=(-35, -80), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)

ax1.annotate('Global infections accelerate again', xy=(23, 800000),  xycoords='data',
                xytext=(-0, -40), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"))
ax1.legend()
plt.show()
fig.savefig('Deaths as a % of Cases & Stringency Levels UK.png')
plt.close()
