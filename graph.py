import pandas as pd
Graph = pd.read_csv('DataCampWork/RDCD2.csv')
print(Graph.columns)
Total_Cases = Graph[["Week_Num", "total_cases", 'total_deaths', "Econ_Block", "location"]]
Countries = Total_Cases[Total_Cases["location"].isin(["Ireland"])]
#EUTotal_Cases = Total_Cases[Total_Cases["Econ_Block"] == 'EU']
print(Countries.columns)
#print(EUTotal_Cases.head)
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.plot(Countries['Week_Num'], Countries[['total_cases', 'total_deaths']])
plt.show()
