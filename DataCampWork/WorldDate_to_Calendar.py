import pandas as pd
date_period = pd.read_csv('countries_of_the_world.csv', index_col=0)
# explore column names
for val in date_period:
    print(val)
print(date_period.columns)
print(date_period[0:1])
print(date_period)
print(date_period.tail)
print(date_period[1:4])
print(date_period.loc[['Albania ', 'Zambia '], ['Region']])
print(date_period.loc[:, ['Region']])
print(date_period.loc[:, :])
sel=[date_period['Region']]
print(sel)
