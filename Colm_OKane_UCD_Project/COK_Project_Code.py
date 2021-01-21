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


print(EU.index)


# Merge EU data into CD Data
CD = (CD.merge(EU, left_on='COUNTRY', right_on='Country', how='inner'))
print(CD.head)
print(CD.columns)
print(CD.isna().sum())
CD.to_csv('CD.csv')