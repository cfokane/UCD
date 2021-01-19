import pandas as pd
#Read CSV's into Project
RD = pd.read_csv('raw_data.csv')
Countries = pd.read_csv('countries_of_the_world.csv')
print(Countries)
print(Countries.isna().sum())

del Countries['Coastline (coast/area ratio)']
del Countries['Net migration']
del Countries['Infant mortality (per 1000 births)']
del Countries['GDP ($ per capita)']
del Countries['Literacy (%)']
del Countries['Phones (per 1000)']
del Countries['Arable (%)']
del Countries['Crops (%)']
del Countries['Other (%)']
del Countries['Climate']
del Countries['Birthrate']
del Countries['Deathrate']
del Countries['Agriculture']
del Countries['Industry']
del Countries['Service']
countries=Countries.rename(columns={'Country':'location'})

print(countries)
print(countries.isna().sum())


#RDArea = (RD.merge(Countries, left_on='location', right_on='Country', how='inner', suffixes=('_RDCD', '_Countries')))
RDArea = (RD.merge(countries, on='location', how='inner', suffixes=('_RD', '_countries')))
#RDCD20 = (RDCD20.merge(CD, on='KEYCODE&DATE', how='outer', suffixes=('_RD', '_CD')))left_on='location', right_on='Country', how='inner', suffixes=('_RDCD', '_Countries')))
print(RDArea)
print(RDArea.isna())
print(RDArea.isna().sum())
RDArea.to_csv('RDArea.csv')


