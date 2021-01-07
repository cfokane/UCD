import numpy as np
import pandas as pd


trans_enhan = pd.read_csv('transformed_data.csv', index_col=0)
for val in trans_enhan :
    print(val)
