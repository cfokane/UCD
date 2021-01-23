import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
from matplotlib import rcParams

data = pd.read_csv('RDCD8.csv', index_col=0)
from matplotlib.pyplot import rcParams
fig, ax =plt.subplots()
#rcParams['figure.figsize']=10,6 # to change size of graph
plt.style.use('ggplot')
ax.plot(data.index, data['Grand_Total'])
ax.set_xlabel('Time')
ax.set_ylabel('Countries with Cases')

plt.show()

#color='m', marker='v', linestyle='-')