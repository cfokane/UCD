import pandas as pd

EU = pd.read_csv('states.csv')
CD = pd.read_csv('transformed_data.csv')
RD = pd.read_csv('raw_data.csv')
#Creat Key
#CD['KEYCODE&DATE'] = CD['CODE'] + CD['DATE']
#RD['DATE'] = pd.to_datetime(RD['date'], format='%Y/%m/%d')
#RD['KEYCODE&DATE'] = RD['iso_code'] + RD['date']
#Countries = pd.read_csv('countries_of_the_world.csv')

# print(RD['DATE'])
# Create Key in RD
# print(RD['KEYCODE&DATE'])
# print(RD.columns)
# print(RD.head)

import pandas as pd
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

CD['DATE'] = pd.to_datetime(CD['DATE'], format='%Y/%m/%d')

# EU['EU_Membership']=(EU['European Union']=='Member')
BRICS = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
condition = CD["COUNTRY"].isin(BRICS)
print(CD[condition])

print('EU_Membership')
print(EU[EU['European Union'] == 'EU_Membership'])
print(EU.columns)
print(EU.head)

# print(EU.index)
# for val in EU :
#    print(val)
EU2=(pd.concat([EU, CD], sort=True))
print(EU2.head(5))
print(EU2.columns)
print(EU2.index)
for val in EU2 :
    print(val)