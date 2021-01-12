import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dogs=pd.read_csv('dogs.csv')
print(dogs)
print(dogs.columns)
print(dogs.index)
dogs_ind =dogs.set_index('Name')
print(dogs_ind)
dogs_ind.reset_index()
#dogs_ind.reset_index(drop=True)
# sort index
dogs_srt =dogs.set_index('Breed', 'Owner').sort_index()
print(dogs_srt)

print(dogs)
print(dogs.groupby('Colour')['Weight_Kg'].mean())
print(dogs.pivot_table(values='Weight_Kg', index='Colour'))
print(dogs.pivot_table(values='Weight_Kg', index='Colour', aggfunc=np.median))
print(dogs.pivot_table(values='Weight_Kg', index='Colour', aggfunc=[np.median, np.sum]))
print(dogs.pivot_table(values='Weight_Kg', index='Colour', columns='Breed'))
print(dogs.pivot_table(values='Weight_Kg', index='Colour', columns='Breed', fill_value=0))
print(dogs.pivot_table(values='Weight_Kg', index='Colour', columns='Breed', fill_value=0, margins=True))


