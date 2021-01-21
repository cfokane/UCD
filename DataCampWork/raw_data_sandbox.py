import pandas as pd
RD= pd.read_csv('raw_data.csv')
print(RD.columns)
RD['KEYCODE&DATE'] = RD['iso_code'] + RD['date']
print(RD['KEYCODE&DATE'])
print(RD.groupby('KEYCODE&DATE').first())
print(RD.groupby('KEYCODE&DATE')['total_cases'].sum())

print(RD.groupby(['iso_code', 'date'])['total_cases'].count())
print(RD.groupby(['iso_code', 'date'])['total_cases'].diff())

#create datasets with weekly data
RD['Weekly_Cases']=(RD.groupby('iso_code')['total_cases'].diff())
RD['Weekly_Deaths']=(RD.groupby('iso_code')['total_deaths'].diff())
#Create a comparible index (1-10) called Stringency_Indexed from Govt'stringency_index' to
RD['Stringency_Indexed']=(RD['stringency_index'] / 10).round()
RD['Stringency Effect on Cases'] = RD['Weekly_Cases'] / RD['Stringency_Indexed'].fillna(0)#Do we need this?

#Timeseries_bool = RD[(RD["date"] >= "2020-01-02") & (RD["date"] <= "2020-03-31")]
RD2=RD[RD['date']>'2020-01-02'] #This works to move start date


print(RD2.groupby('iso_code')['date'].count())
print(RD2.columns)


RD2.to_csv('RDWeekly_Cases.csv')


#can I fill in the blanks with merge-order test below
#RDCDtest = (RD.merge_order(CD, left_on='COUNTRY', right_on='Country', how='inner'))
#print(RDCDtest.head)
#print(RDCDtest.columns)
#print(RDCDtest.isna().sum())

#RD[RD['KEYCODE&DATE']=='total_cases'].groupby('network')['duration'].sum()
#RD['Weekly_Cases'] = (RD.groupby(['KEYCODE&DATE'])[RD.total_cases].diff())