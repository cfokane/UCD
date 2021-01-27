import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('RDCD12c.csv')
print(data)
plt(data).scatter('population', 'AreaKM2', s = ['CasesxArea']*2, alpha=0.8)
plt.xscale('log')
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
plt.xlabel('GDP per Capita in US $')
plt.ylabel('Life Expectancy in Years')
plt.title('World Development in 2007')
#plt.xlim(1, 39) #to set the axis ...xlim for x axis
#plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])
#plt.ylim(0, 4500000) #to set the axis ...xlim for x axis
#plt.yticks([500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000],['0.5m', '1.0m', '1.5m', '2.0m', '2.5m', '3.0m', '3.5m', '4.0m', '4.5m'])

plt.grid(True)
# Additional customizations
#plt.text(1550, 71, 'India')
#plt.text(5700, 80, 'China')
plt.show()
plt.close()