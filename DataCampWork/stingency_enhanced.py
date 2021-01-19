import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

#Read CSV's into Project
CD = pd.read_csv('transformed_data.csv')
RD = pd.read_csv('raw_data.csv')
EU = pd.read_csv('states.csv')
Countries = pd.read_csv('countries_of_the_world.csv')


# Create Key to merge data
CD.sort_values('DATE')
CD['KEYCODE&DATE'] = CD['CODE'] + CD['DATE']
RD.sort_values('date')
RD['KEYCODE&DATE'] = RD['iso_code'] + RD['date']
print(RD['KEYCODE&DATE'])
print(CD['KEYCODE&DATE'])

#Sort rows before creating new data series

#print(RD.columns)
#print(RD.head)
RD['DATE'] = pd.to_datetime(RD['date'], format='%Y/%m/%d')
CD['DATE'] = pd.to_datetime(CD['DATE'], format='%Y/%m/%d')

print(CD.columns)
print(RD.columns)
print(EU.columns)
print(Countries.columns)

print(EU.index)
#    for val in EU :
#    print(val)
#EU2=(pd.concat([RD, Countries, sort=True))
#print(EU2)
# print(EU.head(5))
# print(EU.columns)

# Merge EU data into CD Data
CD = (CD.merge(EU, left_on='COUNTRY', right_on='Country', how='inner'))
print(CD.head)
print(CD.columns)
print(CD.isna().sum())
CD.to_csv('CD.csv')


RDCD = (RD.merge(CD, on='KEYCODE&DATE', how='outer', suffixes=('_RD', '_CD')))
RDCD['DATE'] = pd.to_datetime(RDCD['date'], format='%Y/%m/%d')

# Create Key Fields
RDCD['Week_Num'] = RDCD['DATE'].dt.strftime('%U')
RDCD['day'] = RDCD['DATE'].dt.strftime('%A')
RDCD['dayz'] = RDCD['DATE'].dt.strftime('%j')
RDCD['Dates'] = RDCD['DATE'].dt.strftime('%Y%m%d')
RDCD['Wednesdays'] = RDCD['day'] == 'Wednesday'

# add columns with comparable measures
RDCD['CasesxArea'] = RDCD['total_cases'] / RDCD['Area (km²)']
RDCD['CasesxPop'] = RDCD['total_cases'] / RDCD['population']
RDCD['DeathsxCases'] = RDCD['total_deaths'] / RDCD['total_cases']


# park/remove unneeded rows
del RDCD['Unnamed: 9']
del RDCD['Unnamed: 10']
del RDCD['Unnamed: 11']
del RDCD['Unnamed: 12']
del RDCD['Unnamed: 13']
del RDCD['GDP per capita ($, millions)']
del RDCD['GDP ($, millions)']
del RDCD['GDP (€, millions)']
del RDCD['Population Density']
del RDCD['Population']
del RDCD['Language']
del RDCD['Currency Code']
del RDCD['Currency']
del RDCD['European Monetary Union']
del RDCD['European Single Market']
del RDCD['European Free Trade Agreement']
del RDCD['European Parliament Seats']
del RDCD['Council Votes']
del RDCD['Accession Year']
del RDCD['GDPCAP']
del RDCD['POP']
del RDCD['STI']
del RDCD['TD']
del RDCD['TC']
del RDCD['HDI']
del RDCD['DATE_CD']
del RDCD['COUNTRY']
del RDCD['CODE']
del RDCD['KEYCODE&DATE']
del RDCD['DATE_RD']

# Create groups of Economic Blocks using Dict method
econ_blocks = {
    'Country': ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia',
                'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania',
                'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain',
                'Sweden', 'United Kingdom', 'Brazil', 'Russia', 'India', 'China', 'South Africa', 'United States',
                'Japan'],
    'Econ_Block': ['EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU',
                   'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'BRICS', 'BRICS', 'BRICS', 'BRICS',
                   'BRICS', 'US', 'Japan']}
Econ_BLocks = pd.DataFrame(econ_blocks)
RDCD = (RDCD.merge(Econ_BLocks, left_on='location', right_on='Country', how='outer'))
# check for missing data
print(RDCD.isna().sum())
RDCD.fillna(0)

#Replace Missing Values by filling 'na's with 'No_Affiliation' identifier
RDCD['Econ_Block'] = RDCD['Econ_Block'].fillna('No_Affiliation')
print(RDCD.columns)
print(RDCD.isna().any())
print(RDCD.isna().sum())
# Create a Weekly Dataset using Wednesday data as weekly reporting day
RDCD1=RDCD.query('day == "Wednesday"')
#RDCD1.loc[:, 'Date')
#RDCD2=RDCD1.query('DATE <= 2020-06-30')
#RDCD2=RDCD1.query('DATE > 2020-01-01')
#define 2020 period of analysis
#print(RDCD1.loc[:'Week_Num'])
#RDCD2=RDCD1.query('Week_Num <= "39"')


RDCD.to_csv('RDCD.csv')



RDCD1 = pd.read_csv('RDCD.csv')
del RDCD1['Country_y']
# Calculate Weekly Change in Cases
RDCD1['Weekly_Cases']=(RDCD1.groupby('iso_code')['total_cases'].diff())
RDCD1['Weekly_Deaths']=(RDCD1.groupby('iso_code')['total_deaths'].diff())
#Change Govt'stringency_index' to a more comparable index (1-10) called Stringency_Indexed
RDCD1['Stringency_Indexed']=(RDCD1['stringency_index'] / 10).round()

RDCD1.to_csv('RDCD1.csv')
print(RDCD1.groupby('iso_code')['Week_Num'].count())



RDCD1.to_csv('RDCD1.csv')

RDCD2 = pd.read_csv('RDCD1.csv')

RDCD4=(RDCD1.pivot_table(values='CasesxPop', index='Week_Num', columns='Econ_Block', fill_value=0, margins=True))
RDCD4.to_csv('RDCD4.csv')
#print(RDCD4)

#forward fill for missing entries or 0's where value is missing

#RDCD2EB = RDCD2.groupby('Econ_Block')['total_cases', 'total_deaths', 'Deaths/Cases'].sum()
#print(RDCD2EB)

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
#fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against MONTH
#RDCD2=RDCD2.sort_values(['iso_code', 'Econ_Block', 'Week_Num'])
#ax.plot(RDCD2["date"], RDCD2["total_cases"])
#plt.show()

#print(type('Week_Num'))
# RDCD.groupby('Econ_Block')['Cases/Pop'].mean())
# print(RDCD)


# print(EUCD2.head
# print(EUCD2.columns)
# print(EUCD2.isna().sum())
import numpy as np

#Filter df to Wks1-25 2020

#filter_criteria=((RDCD['Week_Num'] <='25') & (RDCD['Econ_Block'] !='No_Affiliation') & (RDCD['day'] =='Wednesday')  )
#print(RDCD.loc[filter_criteria, ['Cases/Pop', 'population']].mean())

#print(Econ)

import matplotlib.pyplot as plt
#Econ.plot(x='Week_Num', y='Econ_Block', kind='line', rot=45)
#plt.show()

# Drop duplicate store/department combinations
#CODE_Dupes = df.drop_duplicates(subset=["CODE", "COUNTRY"])
#print(CODE_Dupes)

# Subset the rows where Wednesday is True and drop duplicate dates
#Wednesday_only_Data = df[df["Wednesdays"]].drop_duplicates(subset="Wkdayz2")
#print(Wednesday_only_Data)

# Print date col of Wednesday_only_Data
#print(Wednesday_only_Data["Wkdayz2"])

# still need to work out how to exclude the range outside of H1
#RDCD['Active Range'] = RDCD['Week_Num']<=25)

#still need to work out how you are going to report the econ blocks mean or pivot


#OLD CODE
# EU['EU_Membership']=(EU['European Union']=='Member')
#BRICS = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
#condition = CD["COUNTRY"].isin(BRICS)
#print(CD[condition])


#print(EU[EU['European Union'] == 'EU_Membership'])
# COVID_EU2=(EU2.merge(COVID_DATA, left_on='Code', right_on='CODE', how='outer'))
# COVID_EU2['Cases per Head of Pop']=COVID_EU2['TC']/COVID_EU2['Population']

# print(COVID_EU2.head(10))
# print(COVID_EU2.columns)
# print(COVID_EU2.shape)
# print(COVID_EU2.isna().sum())
