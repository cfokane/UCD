import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#plt.style.use('ggplot')
plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD=(data.pivot_table(values=['Weekly_Deaths', 'Weekly_Cases'] , index='Month', columns='Econ_Block', aggfunc='sum',fill_value=0, margins=True).iloc[:-1,:])
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
RD1=RD.reindex(new_order, axis=0)
print(RD1)
RD2 = pd.DataFrame(RD1)
RD2['Deaths_x_Cases'] = RD2['Weekly_Deaths'] / RD2['Weekly_Cases']
print(RD2)



RD2 = RD1.loc[:, ['Econ_Block', 'Month', 'Deaths_x_Cases']]
#print(RD2)

#print(RD2)
#create a pivot table
#RDCD4=(RD.pivot_table(values=['Deaths_x_Cases'] , index='Month', columns='Econ_Block', aggfunc='sum',fill_value=0, margins=True).iloc[:-1,:])
#RDCD4a=RDCD4.fillna(0)

print(RDCD4b)
#RDCD4b.to_csv('RDCD4b.csv')

#print(RDCD4b)

#data = pd.read_csv('RDCD4b.csv', index_col=0)
#print(RDCD4b)
fig, ax = plt.subplots(figsize=(12,5))

#plt.figure(figsize=(6,4))
#seventies = climate_change["1970-01-01":"1979-12-31"]
#ax.plot(seventies.index, seventies["co2"])
#plt.rcParams["figure.figsize"]=(200,60)

ax.plot(RD.index, RD['BRICS'], label='BRICS')
ax.plot(RD.index, RD['EU'], label='EU')
ax.plot(RD.index, RD['US'], label='US')
ax.plot(RD.index, RD['All_Others'], label='All Others')
#ax.plot(data.index, data['All'], label='All Countries')
ax.set_xlabel('2020 by Month')
ax.set_ylabel("Deaths as % of Monthly Cases by Block")
plt.ylim(0, 30) #to set the axis ...xlim for x axis
plt.yticks([5, 10, 15, 20, 25, 30],['5%', '10%', '15%', '20%', '25%', '30%'])

ax.set_title("COVID Deaths as % of Cases for selected Economic Blocks Q1-Q3 2020")

ax.annotate('Peak in Mortality Rate @ 23% Cases - All Other Countries', xy=(3, 23),  wrap=True, xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('EU 5.3%', xy=(3, 5.3),  wrap=True, xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('EU 6.1%', xy=(4, 6.1),  wrap=True, xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('EU 6.0%', xy=(5, 6.0),  wrap=True, xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.annotate('EU 6.4%', xy=(6, 6.4),  wrap=True, xycoords='data',
                xytext=(-1, 10), textcoords='offset points',
                arrowprops=dict(arrowstyle="->")
                )
ax.legend(loc=2)

plt.show()
fig.savefig('Deaths as Proportion of Cases by Econ Blocks.png')
plt.close()