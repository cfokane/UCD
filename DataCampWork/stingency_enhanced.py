import pandas as pd
df = pd.read_csv('stringency.csv', index_col=0)
for val in df :
    print(val)
print(df.head(10))