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
plt.grid(True)
# Additional customizations
#plt.text(1550, 71, 'India')
#plt.text(5700, 80, 'China')
plt.show()