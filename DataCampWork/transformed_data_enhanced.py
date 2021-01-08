from typing import Any, Union

import pandas as pd
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

df = pd.read_csv('transformed_data.csv')
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y/%m/%d')
# Create Keys
df['Week_Num'] = df['DATE'].dt.strftime('%U')
df['day'] = df['DATE'].dt.strftime('%A')
df['dayz'] = df['DATE'].dt.strftime('%j')
df['Dates'] = df['DATE'].dt.strftime('%Y%m%d')
# concatenate columns for Keys from Country Code Week and Day numbers
df['Wkdayz'] = df['Week_Num'] + df['dayz']
df['Con_cat'] = df['CODE'] + df['Wkdayz']
df['Cases per M Pop'] = df['TC'] / df['POP']
for val in df:
    print(val)
print(df)
print(df.head(10))

#for lab, row in df.iterrows() :
#   print(lab)
#   print(row)
#df = pd.read_csv('transformed_data.csv', index_col=0)
#for lab, row in df.iterrows() :
#     print(lab + ": " + str(row['COUNTRY']))

#df= pd.read_csv('transformed_data.csv', index_col = 0)
#for lab, row in df.iterrows() :
#    df.loc[lab, 'COUNTRYS'] = row['index_col=0'].upper()
#    df.loc[lab,'key_'] = df['CODE'] + df['Wkdayz']
#    print(df)