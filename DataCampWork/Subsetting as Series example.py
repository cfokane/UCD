import pandas as pd
RDSB= pd.read_csv('RDCD2.csv')
print(RDSB.columns)
print(RDSB)

#elect pandas series using .loc
EU_Only=RDSB.loc[:,'Econ_Block'] =='EU'
print(RDSB[EU_Only])

