import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD = data.loc[:, ['location', 'Econ_Block', 'Week_Num', 'total_cases',
                  'Stringency_Indexed', 'population', 'total_deaths',
                  'DeathsxCases']]
RD = pd.DataFrame(RD)
RD.fillna(0)
#RDEcon = RD.query('Week_Num== "39"')
#RDIre = RDEcon.query('location == "Ireland"')
print(RD)

sns.set(style='whitegrid')
# Chart showing Case numbers over time, against number of deaths
g=sns.relplot(x='total_deaths', y='total_cases', data=RD, kind='scatter', height=5, aspect=1.75, size='Econ_Block', hue='Econ_Block')
#g= sns.relplot(x='Week_Num', y='Weekly_Cases', data=RDIre, size='Weekly_Deaths', height=5, aspect=1.75, hue='Weekly_Deaths', legend='full')
g.fig.suptitle('Blocks Countries; Cases & Deaths', x=0.5, y=1.0)
plt.subplots_adjust(top=0.85)
#leg=g._legend
#leg.set_bbox_to_anchor([0.5, 0.5])
#leg._loc=2
#fig=ax.get_figure()
#fig.savegig('Ireland; Cases & Deaths.png')
plt.savefig('Econ Block; Cases & Deaths.png')
plt.show()
