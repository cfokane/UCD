import pandas as pd
RDCD2 = pd.read_csv('RDCD1.csv')
print(RDCD2.columns)


#RDCD2.groupby('iso_code')['Week_Num']
#RDCD2=[(RDCD2['Econ_Block']!='EU') & (RDCD2['Week_Num']<=39) & (RDCD2['Weekly_Cases']) & (RDCD2['total_cases'])]
#print(RDCD2)
#dogs=[ (dogs[‘breed’]==‘Labrador’) & (dogs[‘colour’]==‘brown’) ]

import matplotlib.pyplot as plt
import seaborn as sns
# Create a scatter plot of absences vs. final grade
#sns.scatterplot(x='', y='Weekly_Cases', data=RDCD1, size='Weekly_Cases', hue='Weekly_Cases', alpha=0.4)
#time, cases or deaths and stringency indexed 1-5
# Show plot
#What is the data=RDCD2 about above
#fig, ax = plt.subplots()
#ax.plot(RDCD2["Stringency_Indexed"], RDCD2["Weekly_Cases"],
#       color='r', marker='o', linestyle='--')
#plt.show()

# Read the data from file using read_csv
Weekly_Cases = pd.read_csv('RDCD2.csv', parse_dates=["date"], index_col="Week_Num")

print(Weekly_Cases.head())
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(Weekly_Cases.index, Weekly_Cases['Weekly_Cases'])

# Set the x-axis label
ax.set_xlabel('Time') #where time is a preset as the index ie Week_Num

# Set the y-axis label
ax.set_ylabel('Weekly Cases')

# Show the figure
plt.show()
