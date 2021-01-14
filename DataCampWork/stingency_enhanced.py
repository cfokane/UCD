import pandas as pd
CSI = pd.read_csv('covid-stringency-index.csv')
E_U = pd.read_csv('states.csv')
COVID_DATA = pd.read_csv('transformed_data.csv')
CSI['CODE&DATE']=CSI['Code']+CSI['Date']
COVID_DATA['CODE&DATE']=COVID_DATA['CODE']+COVID_DATA['DATE']
CSI['DATE'] = pd.to_datetime(CSI['Date'], format='%Y/%m/%d')
print(CSI.columns)
#print(COVID_DATA.columns)
print(CSI)
#print(S_E.columns)
#print(E_U.columns)
# print(S_E.head(5))
# print(S_E.info())
# print(S_E.describe())
# print(S_E.shape)
# print(S_E.index)
# for val in S_E :
#    print(val)
#EU=(pd.concat([S_E, E_U], sort=True))
#print(EU.head(5))
#print(EU.columns)

#EU2=(S_E.merge(E_U, left_on='Entity', right_on='Country', how='outer'))
#print(EU2.head(10))
#print(EU2.columns)
#COVID_EU2=(EU2.merge(COVID_DATA, left_on='Code', right_on='CODE', how='outer'))
#COVID_EU2['Cases per Head of Pop']=COVID_EU2['TC']/COVID_EU2['Population']

#print(COVID_EU2.head(10))
#print(COVID_EU2.columns)
#print(COVID_EU2.shape)
#print(COVID_EU2.isna().sum())
#COVID_EU2.to_csv('with_Cases_per_Head_of_Pop.csv')
#import matplotlib.pyplot as plt
#COVID_EU2.plot(x='STI',y='Date', kind='line')
#plt.show()
