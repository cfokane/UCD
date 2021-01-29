import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCDFinal.csv', index_col=0)
print(data.columns)
RD = data.loc[:, ['location', 'Econ_Block', 'Week_Num', 'Weekly_Cases',
                  'Stringency_Indexed', 'population', 'Weekly_Deaths',
                  'DeathsxCases']]
RDEcon = RD.query('Econ_Block== "EU"')
RDEcon = RDEcon.query('location == "Ireland"')
#RDEcon['Week_Case']=(RDEcon['Weekly_Cases'] **3)
RDEcon = pd.DataFrame(RDEcon)
print(RDEcon)

sns.set(style='whitegrid')
# Chart showing Case numbers over time, against number of deaths
g= sns.relplot(x='Week_Num', y='Weekly_Cases', data=RDEcon, size='Weekly_Cases', height=2.8, aspect=1.5, hue='Weekly_Deaths')
g.fig.suptitle('Ireland; Cases & Deaths', x=0.5, y=1.0)
plt.subplots_adjust(top=0.85)
#leg=g._legend
#leg.set_bbox_to_anchor([0.5, 0.5])

#leg._loc=2
#fig=ax.get_figure()
#fig.savegig('Ireland; Cases & Deaths.png')
plt.savefig('Ireland; Cases & Deaths.png')
plt.show()
