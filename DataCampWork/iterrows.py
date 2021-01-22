import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

#Read CSV's into Project
RD = pd.read_csv('raw_data.csv')
print(RD.columns)
#print(next(RD.iterrows()))
#for index, row in RD.head(n=2).iterrows():
#     print(index, row)

#for index, row in RD.head().iterrows():
         # access data using column names
#         print(index, row['date'], row['total_cases'], row['total_deaths'])
