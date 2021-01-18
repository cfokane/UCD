import pandas as pd
Graph = pd.read_csv('DataCampWork/RDCD2.csv')
print(Graph.columns)
Total_Cases = Graph[["Week_Num", "Weekly_Cases", 'Weekly_Deaths', "Econ_Block", "location"]]
Countries = Total_Cases[Total_Cases["location"].isin(["Italy"])]
#Total_Cases2=Total_Cases[["Econ_Block", "total_cases"]].groupby("Econ_Block").mean()
#EUTotal_Cases = Total_Cases[Total_Cases["Econ_Block"] == 'EU']
print(Total_Cases)
#print(EUTotal_Cases.head)
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#fig, ax = plt.subplots()
#plt.style.use('ggplot')
#ax.plot(Countries['Week_Num'], Countries[['Weekly_Deaths', 'Weekly_Deaths']])
#ax.set_ylabel(["Infections"])
#ax.set_xlabel("Week Number")
#ax.legend()

#plt.show()

plt.style.use('ggplot')
fig, ax = plt.subplots()
plt.style.use('ggplot')
ax.scatter(Countries['Week_Num'], Countries['Weekly_Deaths'])
ax.set_ylabel(["Infections"])
ax.set_xlabel("Week Number")
ax.legend()

plt.show()
