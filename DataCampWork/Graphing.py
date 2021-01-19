import numpy as np
import pandas as pd
EU = pd.read_csv('RDCD2.csv')
print(EU.columns)
print(EU.head)
import matplotlib.pyplot as plt
import seaborn as sns
# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='Week_Num', y='total_cases', data=EU, size='total_cases', hue='total_cases', alpha=0.4)
#time, cases or deaths and stringency indexed 1-5
# Show plot
plt.show()