import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader

#Read CSV's into Project
RD = pd.read_csv('raw_data.csv')
print(RD.columns)

