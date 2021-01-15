import pandas as pd
EU = pd.read_csv('states.csv')
CD = pd.read_csv('transformed_data.csv')
RD = pd.read_csv('raw_data.csv')
CD['KEYCODE&DATE']=CD['CODE']+CD['DATE']
RD['DATE'] = pd.to_datetime(RD['date'], format='%Y/%m/%d')
RD['KEYCODE&DATE']=RD['iso_code']+RD['date']
Countries = pd.read_csv('countries_of_the_world.csv')

#print(RD['DATE'])
# Create Key in RD
print(RD['KEYCODE&DATE'])
print(RD.columns)
print(RD.head)

import pandas as pd
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader



CD['DATE'] = pd.to_datetime(CD['DATE'], format='%Y/%m/%d')
# Create Key Fields
#CD['Week_Num'] = CD['DATE'].dt.strftime('%U')
#CD['day'] = CD['DATE'].dt.strftime('%A')
#CD['dayz'] = CD['DATE'].dt.strftime('%j')
#CD['Dates'] = CD['DATE'].dt.strftime('%Y%m%d')
#CD['Wednesdays']=CD['day'] =='Wednesday'

#print(CD.columns)
#print(CD.head)

#EU['EU_Membership']=(EU['European Union']=='Member')
BRICS=['Brazil', 'Russia', 'India', 'China', 'South Africa']
condition = CD["COUNTRY"].isin(BRICS)
print(CD[condition])

print('EU_Membership')
print(EU[EU['European Union']=='EU_Membership'])
print(EU.columns)
print(EU.head)

# print(S_E.info())
# print(S_E.describe())
# print(S_E.shape)
# print(S_E.index)
# for val in S_E :
#    print(val)
#EU=(pd.concat([S_E, E_U], sort=True))
#print(EU.head(5))
#print(EU.columns)

#Merge EU data into CD Data
CD=(CD.merge(EU, left_on='COUNTRY', right_on='Country', how='inner'))
print(CD.head)
print(CD.columns)
print(CD.isna().sum())
CD.to_csv('CD.csv')


#COVID_EU2=(EU2.merge(COVID_DATA, left_on='Code', right_on='CODE', how='outer'))
#COVID_EU2['Cases per Head of Pop']=COVID_EU2['TC']/COVID_EU2['Population']

#print(COVID_EU2.head(10))
#print(COVID_EU2.columns)
#print(COVID_EU2.shape)
#print(COVID_EU2.isna().sum())

#import matplotlib.pyplot as plt
#COVID_EU2.plot(x='STI',y='Date', kind='line')
#plt.show()

RDCD=(RD.merge(CD, on='KEYCODE&DATE', how='outer', suffixes=('_RD', '_CD')))
RDCD['DATE'] = pd.to_datetime(RDCD['date'], format='%Y/%m/%d')
# Create Key Fields
RDCD['Week_Num'] = RDCD['DATE'].dt.strftime('%U')
RDCD['day'] = RDCD['DATE'].dt.strftime('%A')
RDCD['dayz'] = RDCD['DATE'].dt.strftime('%j')
RDCD['Dates'] = RDCD['DATE'].dt.strftime('%Y%m%d')
RDCD['Wednesdays']=RDCD['day'] =='Wednesday'



#del RDCD['Unnamed: 9']
#del RDCD['Unnamed: 10']
#del RDCD['Unnamed: 11']
#del RDCD['Unnamed: 12']
#del RDCD['Unnamed: 13']
#del RDCD['GDP per capita ($, millions)']
#del RDCD['GDP ($, millions)']
#del RDCD['GDP (€, millions)']
#del RDCD['Population Density']
#del RDCD['Population']
#del RDCD['Language']
#del RDCD['Currency Code']
#del RDCD['Currency']
#del RDCD['European Monetary Union']
#del RDCD['European Single Market']
#del RDCD['European Free Trade Agreement']
#del RDCD['European Parliament Seats']
#del RDCD['Council Votes']
#del RDCD['Accession Year']
#del RDCD['GDPCAP']
#del RDCD['POP']
#del RDCD['STI']
#del RDCD['TD']
#del RDCD['TC']
#del RDCD['HDI']
#del RDCD['DATE_CD']
#del RDCD['COUNTRY']
#del RDCD['CODE']
#del RDCD['KEYCODE&DATE']
#del RDCD['DATE_RD']

print(RDCD.head)
print(RDCD.columns)
print(RDCD.isna().sum())
RDCD.to_csv('RDCD.csv')


#print(EUCD2.head
#print(EUCD2.columns)
#print(EUCD2.isna().sum())