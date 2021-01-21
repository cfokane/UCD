import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

RDSB= pd.read_csv('RDCD1.csv', index_col=0)
print(RDSB.columns)
print(RDSB)
print(RDSB.index)
#Select pandas df of key column info using .loc
Key_Columns_Only = RDSB.loc[:, ['location', 'DATE_RD', 'Month', 'Wednesdays','total_cases', 'total_deaths', 'Week_Num', 'Weekly_Cases', 'Weekly_Deaths', 'Econ_Block','Stringency_Indexed', 'day', 'date']]
print([Key_Columns_Only])
#convert to csv
Key_Columns_Only.to_csv('Key_Columns_Only.csv')



#Key_Columns_Only[np.logical_or('Stringency_Indexed'>=4, 'total_deaths'>=500)]
#print([Key_Columns_Only])

#Read CSV and index on Date_RD
KCO = pd.read_csv('Key_Columns_Only.csv', index_col=2)

#filtering the new df
#by Euro_Block
is_huge=KCO['Stringency_Indexed'] >=3
print(KCO[is_huge])
print(KCO[is_huge].columns)
is_Ireland=KCO['location'] =='Ireland'
print(KCO[is_Ireland])
#is_EU=KCO['Econ_Block'] =='EU'
#rint(KCO[is_EU])
is_Wed=KCO['Wednesdays'] ==True
print(KCO[is_Wed])


#TD = KCO['total_deaths']
#between = np.logical_and(TD > 100, TD < 50000)
#medium=TD[between]
#print(medium)

#fig, ax = plt.subplots()
#plt.style.use('ggplot')
#ax.scatter(KCO['Month'], KCO['total_deaths'])
#ax.set_ylabel(["Infections"])
#ax.set_xlabel("Month")
#ax.legend()
#plt.show()




#KCO2[np.logical_and(KCO['is_Wed'], KCO['is_EU'])]
#print(KCO2)
#if statement
#if Key_Columns_Only('location') =='Ireland' :
#    print("result")

#High_Deaths = RDSB.loc[:,'Weekly_Deaths'] >=2000
#Germany = RDSB.loc[:,'location'] =='Germany'
#Starting= RDSB.loc[:,'Week_Num'] >=1

#print(RDSB[EU_Only])

#RDSB[High_Deaths].to_csv('High_Deaths.csv')RDSB[Starting].to_csv('Starting.csv')


#Weeks =(RDSB['Weekly_Deaths'] > 10000)
#RDSB[np.logical_and(RDSB['Week_Num'] >=5, RDSB['Week_Num']<39)]
#print(Weeks)
