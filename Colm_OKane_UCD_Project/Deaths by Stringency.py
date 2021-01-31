import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#plt.style.use('ggplot')
plt.style.use('seaborn-whitegrid')

data = pd.read_csv('RDCDFinal.csv')
print(data.columns)
plt.figure();
df2=data(['Stringency_Indexed', 'Weekly_Cases'])
df2.plot(kind='bar');

#RD=data.query('location == "United Kingdom"')
print(df2)