import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD = data.loc[:, ['European Union', 'location',  'Econ_Block', 'Week_Num', 'Weekly_Cases',
                  'Stringency_Indexed', 'population', 'Weekly_Deaths',
                  'DeathsxCases']]
RD = RD.query('Econ_Block== "EU"')
RD.sort_values('European Union')
RD['European Union Status'] = RD['location'] + ' ' + RD['European Union']
RD = pd.DataFrame(RD)
RD.fillna(0)
#RDEcon = RD.query('Econ_Block== "EU"')
#RDIre = RDEcon.query('location == "Ireland"')
print(RD)

sns.set(style='whitegrid')
# Chart showing Case numbers over time, against number of deaths
g=sns.relplot(x='Week_Num', y='European Union Status', data=RD, kind='scatter', height=6.5, aspect=1.75, size='Weekly_Cases', hue='DeathsxCases')
#g= sns.relplot(x='Week_Num', y='Weekly_Cases', data=RDIre, size='Weekly_Deaths', height=5, aspect=1.75, hue='Weekly_Deaths', legend='full')
g.fig.suptitle('EU Countries; Cases & Deaths', x=0.5, y=1.0)
plt.subplots_adjust(top=0.98)

#leg=g._legend
#leg.set_bbox_to_anchor([0.5, 0.5])
#leg._loc=2
#fig=ax.get_figure()
#fig.savegig('Ireland; Cases & Deaths.png')
plt.savefig('EU; Cases & Deaths.png')
plt.show()
plt.clf()