import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import rcParams


#How do you get the row data on the bottom and the Grand Total Data in the Bins data


#data = pd.read_csv('RDCD9.csv')
#fig, ax =plt.subplots()
#bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
#data.iloc[38].hist(bins=bins)
#ax.hist(data['location'], label='Level 5')
#ax.set_xlabel("Stringency 4&5")
#ax.legend
#ax.set_title("Countries at higher Stringency Levels")
#plt.show()

data = pd.read_csv('RDCD9.csv')
fig, ax =plt.subplots()
plt.hist(data, bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39], label 'XXX')
plt.show()
#data.iloc[38].hist(bins=bins)
#ax.hist(data['location'], label='Level 5')
#ax.set_xlabel("Stringency 4&5")
#ax.legend
#ax.set_title("Countries at higher Stringency Levels")
#plt.show()