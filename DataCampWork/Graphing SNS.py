import numpy as np
import pandas as pd
EU = pd.read_csv('RDCD2.csv')
print(EU.columns)
print(EU.head)
import matplotlib.pyplot as plt
import seaborn as sns
# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='stringency_index', y='Weekly_Cases', data=EU, hue='Weekly_Deaths')

sns.relplot(x="Week_Num", y="Weekly_Cases",
                data=EU,
                kind='line', row='Econ_Block', ci='sd')

# Show plot
plt.show()