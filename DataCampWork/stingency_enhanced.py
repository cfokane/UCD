import pandas as pd
df = pd.read_csv('covid-stringency-index.csv', index_col=0)
print(df)

for val in df :
    print(val)
print(df.head(3))
print(df.info())
print(df.describe())

#print(df.shape)
print(df.columns)
#print(df.index)