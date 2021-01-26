import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

#Read CSV's into Project
CD = pd.read_csv('transformed_data.csv')
RD = pd.read_csv('raw_data.csv')
EU = pd.read_csv('states.csv')
Countries = pd.read_csv('countries_of_the_world.csv')


# Create Key to merge data together
CD.sort_values('DATE')
CD['KEYCODE&DATE'] = CD['CODE'] + CD['DATE']
RD.sort_values('date')
RD['KEYCODE&DATE'] = RD['iso_code'] + RD['date']
print(RD['KEYCODE&DATE'])
print(CD['KEYCODE&DATE'])

#Sort rows before creating new data series
RD['DATE'] = pd.to_datetime(RD['date'], format='%Y/%m/%d')
CD['DATE'] = pd.to_datetime(CD['DATE'], format='%Y/%m/%d')



print(CD.columns)
print(RD.columns)
print(EU.columns)



# Merge EU data into CD Data
CD = (CD.merge(EU, left_on='COUNTRY', right_on='Country', how='inner'))
print(CD.head)
print(CD.columns)
print(CD.isna().sum())

CD.to_csv('CD.csv')

# Merge enlarged CD dataset with RD dataset
RDCD = (RD.merge(CD, on='KEYCODE&DATE', how='outer', suffixes=('_RD', '_CD')))

#Create new fields re Dates
RDCD['DATE'] = pd.to_datetime(RDCD['date'], format='%Y/%m/%d')
print(RDCD['date'])
# Create Key Fields
RDCD['Week_Num'] = RDCD['DATE'].dt.strftime('%U') #number of the week in the year
RDCD['Month'] = RDCD['DATE'].dt.strftime('%b') #short name of the month
RDCD['day'] = RDCD['DATE'].dt.strftime('%A') #day of the week
RDCD['dayz'] = RDCD['DATE'].dt.strftime('%j') #number of the day in the year
RDCD['Dates'] = RDCD['DATE'].dt.strftime('%Y%m%d') #dont think this is doing anything useful
RDCD['Wednesdays'] = RDCD['day'] == 'Wednesday' #boolean set to confirm Wednesday as True

# add columns with comparable measures
RDCD['CasesxArea'] = RDCD['total_cases'] / RDCD['Area (km²)']
RDCD['CasesxPop'] = RDCD['total_cases'] / RDCD['population']
RDCD['DeathsxCases'] = RDCD['total_deaths'] / RDCD['total_cases']
print(RDCD)

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
del RDCD['COUNTRY']
del RDCD['CODE']
del RDCD['KEYCODE&DATE']
#del RDCD['DATE_RD']
#del RDCD['DATE_CD']

# Create groups of Economic Blocks from Dictionary
econ_blocks = {
    'Country': ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia',
                'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania',
                'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain',
                'Sweden', 'United Kingdom', 'Brazil', 'Russia', 'India', 'China', 'South Africa', 'United States',
                'Japan'],
    'Econ_Block': ['EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU',
                   'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'EU', 'BRICS', 'BRICS', 'BRICS', 'BRICS',
                   'BRICS', 'US', 'Japan']}
#convert econ_block to dataframe
Econ_BLocks = pd.DataFrame(econ_blocks)
print(Econ_BLocks)
# Merge Econ_BLocks dataset to enhance RDCD dataset
RDCD = (RDCD.merge(Econ_BLocks, left_on='location', right_on='Country', how='outer'))

# check for missing data
#print(RDCD.isna().any())
print(RDCD.isna().sum())


#Replace Missing Values by filling 'na's with 'No_Affiliation' identifier
RDCD.fillna(0)
RDCD['Econ_Block'] = RDCD['Econ_Block'].fillna('No_Affiliation')

print(RDCD.isna().sum())
print(RDCD)

# Create a Weekly Dataset to using Wednesday as the filter to give a weekly reporting day
RDCD=RDCD.query('day == "Wednesday"')


print(RDCD)
print(RDCD.isna().any())
print(RDCD.isna().sum())
print(RDCD.dtypes)


#output this to csv
RDCD.to_csv('RDCD.csv')

# import this as csv
RDCD1 = pd.read_csv('RDCD.csv')
#mask = (RDCD['DATE_CD'] > '2020-01-07') & (RDCD['DATE_CD'] < '2020-09-30')
#Date_Range=RDCD.loc[mask]
#print(Date_Range)



del RDCD1['Country_y']
del RDCD1['Unnamed: 0']



# Calculate Weekly Change in Cases & Deaths from cumulative data within dataset
RDCD1['Weekly_Cases']=(RDCD1.groupby('iso_code')['total_cases'].diff())
RDCD1['Weekly_Deaths']=(RDCD1.groupby('iso_code')['total_deaths'].diff())

#Change Govt'stringency_index' measure to a comparable index (0-5) called Stringency_Indexed
RDCD1['Stringency_Indexed']=(RDCD1['stringency_index'] / 5).round()



group=(RDCD1.groupby('iso_code')['Week_Num'].count())
print(group)
#select date range to analyse

RDCD1=RDCD1.query("DATE_RD >= '2020-01-07' and DATE_RD <='2020-09-30'")

print(RDCD1.dtypes)

#output this to csv
RDCD1.to_csv('RDCD11.csv') #being used by subsetting .loc to create Key_columns_Only.csv

RDCD2 = pd.read_csv('RDCD11.csv', parse_dates=["DATE_RD"])



#create a pivot table
RDCD4=(RDCD2.pivot_table(values='Weekly_Cases', index='Week_Num', columns='Econ_Block', aggfunc='sum',fill_value=0, margins=True))
RDCD4.to_csv('RDCD4.csv')
print(RDCD4)

RDCD5=(RDCD2.pivot_table(values='Weekly_Deaths', index='Week_Num', columns='Econ_Block', aggfunc='sum', fill_value=0, margins=True))
RDCD5.to_csv('RDCD5.csv')
print(RDCD5)

RDCD6=(RDCD2.pivot_table(values='Weekly_Cases', index=['Month'], columns=['Econ_Block'], aggfunc='sum', fill_value=0, margins=False))
new_order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
RDCD6a=RDCD6.reindex(new_order, axis=0)
RDCD6a.to_csv('RDCD6a.csv')
print(RDCD6a)

RDCD7=(RDCD2.pivot_table(values=['Weekly_Cases','Weekly_Deaths'] , index=['Week_Num'], aggfunc='sum', fill_value=0))
RDCD7.to_csv('RDCD7.csv')
print(RDCD7)

RDCD8=(RDCD2.pivot_table(values='Weekly_Deaths', index='Week_Num', columns='location', aggfunc='count', fill_value=0, margins=True, margins_name='Grand_Total').iloc[:-1,:])
RDCD8.to_csv('RDCD8.csv')
print(RDCD8)

#import pivot_ui as pivot_ui
#pivot_ui(RDCD6,outfile_path='pivotRDCD7.html')
#HTML('pivotRDCD7.html')

#RDCD5=(RDCD1.pivot(index='Week_Num', columns='Econ_Block',values='Weekly_Cases'))
#RDCD5.to_csv('RDCD5.csv')
#print(RDCD5)

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


#RDCD1.loc[:, 'Date')
#RDCD2=RDCD1.query('DATE <= 2020-06-30')
#RDCD2=RDCD1.query('DATE > 2020-01-01')
#define 2020 period of analysis
#print(RDCD1.loc[:'Week_Num'])
#RDCD2=RDCD1.query('Week_Num <= "39"')