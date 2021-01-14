import pandas as pd
EU = pd.read_csv('states.csv')
CD = pd.read_csv('transformed_data.csv')
CD['KEYCODE&DATE']=CD['CODE']+CD['DATE']

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
