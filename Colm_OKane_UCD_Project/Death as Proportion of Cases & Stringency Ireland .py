import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#plt.style.use('ggplot')
plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv')
RD=data.query('location == "Ireland"')
print(RD.columns)


RD=(RD.pivot_table(values=['Deaths_%_Cases', 'Stringency_Indexed'] , index='Week_Num', columns='location', aggfunc='sum',fill_value=0, margins=False).iloc[:-1,:])
#new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
#RD1=RD.reindex(new_order, axis=0)
print(RD.columns)



#RD2 = RD1.loc[:, ['Deaths_%_Cases','Stringency_Indexed', 'Month', 'location']]
#print(RD2)

fig, ax = plt.subplots(figsize=(12,5))
plt.style.use('seaborn-whitegrid')
ax.plot(RD.index, RD['Deaths_%_Cases'], color='b', label='Deaths_%_Cases')
ax.set_ylabel('Deaths_%_Cases', color='b')
ax.tick_params('y', colors='blue')
#plt.xlim(, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.ylim(0, 20) #to set the axis ...xlim for x axis
#plt.yticks([500000, 1000000, 1500000, 2000000, 2500000],['0.5m', '1.0m', '1.5m', '2.0m', '2.5m'])
ax2 = ax.twinx()
ax2.plot(RD.index, RD['Stringency_Indexed'], color='red', label='Stringency_Indexed')
ax2.set_ylabel('Stringency_Indexed', color='red')
ax2.tick_params('y', colors='red')
ax.set_title('Deaths as a % of Cases & Stringency Levels Ireland')
ax2.annotate('Over 7 in 100 people with disease are dying', xy=(18, 7.2),  xycoords='data',
                xytext=(-35, -80), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"), wrap=True)

ax.annotate('Global infections accelerate again', xy=(23, 800000),  xycoords='data',
                xytext=(-0, -40), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"))

ax.legend()
plt.show()
fig.savefig('Deaths as a % of Cases & Stringency Levels Ireland.png')
plt.close()
