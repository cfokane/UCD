import pandas as pd
df = pd.read_csv('transformed_data.csv', index_col=0)
for val in df :
    print(val)

df['DATE'] = pd.to_datetime(df['DATE'], format='%Y/%m/%d')
df['Week_Num'] = df['DATE'].dt.strftime('%U')
df['day'] = df['DATE'].dt.strftime('%A')
df['date'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y')
print(df.head(10))

df['dates'] = pd.to_datetime(df['DATE'], format='%Y %m %d')
print(df.head(10))


