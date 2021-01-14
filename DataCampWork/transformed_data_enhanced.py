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
df['Wednesdays']=df['day'] =='Wednesday'
# concatenate columns for Keys from Country Code Week and Day numbers
#df['Wkdayz'] = df['Week_Num'] + df['dayz']
#df['Con_cat'] = df['CODE'] + df['Wkdayz']
#df['Cases per M Pop'] = df['TC'] / df['POP']


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
# Alternative concatenation method to create unique code by country
df['Wkdayz'] = df.Week_Num.str.cat(df.dayz)
df['Wkdayz2'] = df.CODE.str.cat(df.Wkdayz)
for val in df:
    print(val)
print(df)
print(df.head(10))
print(df['day'])

print(df)


# Drop duplicate store/department combinations
#CODE_Dupes = df.drop_duplicates(subset=["CODE", "COUNTRY"])
#print(CODE_Dupes)

# Subset the rows where Wednesday is True and drop duplicate dates
#Wednesday_only_Data = df[df["Wednesdays"]].drop_duplicates(subset="Wkdayz2")
#print(Wednesday_only_Data)

# Print date col of Wednesday_only_Data
#print(Wednesday_only_Data["Wkdayz2"])


