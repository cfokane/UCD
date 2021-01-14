import pandas as pd
EU = pd.read_csv('states.csv')
CD = pd.read_csv('transformed_data.csv')
CD1 = pd.read_csv('raw_data.csv')
CD['KEYCODE&DATE']=CD['CODE']+CD['DATE']
Countries = pd.read_csv('countries_of_the_world.csv')

print(CD1.columns)
print(CD1.head)


import pandas as pd
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

#CD1['DATE'] = pd.to_datetime(CD1['date'], format='%Y/%m/%d')
# Create Keys
#CD1['Week_Num'] = CD1['date'].dt.strftime('%U')
#CD1['day'] = CD1['date'].dt.strftime('%A')
#CD1['dayz'] = CD1['date'].dt.strftime('%j')
#CD1['Dates'] = CD1['date'].dt.strftime('%Y%m%d')
#CD1['Wednesdays']=CD1['day'] =='Wednesday'
#print(CD1.columns)
#print(CD1.head)


CD['DATE'] = pd.to_datetime(CD['DATE'], format='%Y/%m/%d')
# Create Keys
CD['Week_Num'] = CD['DATE'].dt.strftime('%U')
CD['day'] = CD['DATE'].dt.strftime('%A')
CD['dayz'] = CD['DATE'].dt.strftime('%j')
CD['Dates'] = CD['DATE'].dt.strftime('%Y%m%d')
CD['Wednesdays']=CD['day'] =='Wednesday'
#CSI['DATE'] = pd.to_datetime(CSI['Date'], format='%Y/%m/%d')
print(EU.columns)
print(EU.head)
print(CD.columns)
print(CD.head)

#EU['EU_Membership']=(EU['European Union']=='Member')
BRICS=['Brazil', 'Russia', 'India', 'China', 'South Africa']
condition = CD["COUNTRY"].isin(BRICS)
print(CD[condition])

print('EU_Membership')
print(EU[EU['European Union']=='EU_Membership'])
print(CD['DATE'])
print(CD['KEYCODE&DATE'])

# print(S_E.info())
# print(S_E.describe())
# print(S_E.shape)
# print(S_E.index)
# for val in S_E :
#    print(val)
#EU=(pd.concat([S_E, E_U], sort=True))
#print(EU.head(5))
#print(EU.columns)

EUCD2=(CD.merge(EU, left_on='COUNTRY', right_on='Country', how='inner'))
print(EUCD2.head)
print(EUCD2.columns)
print(EUCD2.isna().sum())

EUCD2.to_csv('EUCD2.csv')

#COVID_EU2=(EU2.merge(COVID_DATA, left_on='Code', right_on='CODE', how='outer'))
#COVID_EU2['Cases per Head of Pop']=COVID_EU2['TC']/COVID_EU2['Population']

#print(COVID_EU2.head(10))
#print(COVID_EU2.columns)
#print(COVID_EU2.shape)
#print(COVID_EU2.isna().sum())

#import matplotlib.pyplot as plt
#COVID_EU2.plot(x='STI',y='Date', kind='line')
#plt.show()




print(EUCD2.head)
print(EUCD2.columns)
print(EUCD2.isna().sum())