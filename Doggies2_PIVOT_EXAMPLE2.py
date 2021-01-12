import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dogs=pd.read_csv('dogs.csv')
print(dogs)
print(dogs.columns)
print(dogs.index)
dogs_ind =dogs.set_index('Name')
print(dogs_ind)
print(dogs_ind.loc[['Bella', 'Coco']])
dogs_ind2 =dogs.set_index('Breed')
print(dogs_ind2)
print(dogs_ind2.loc[['Labrador', 'Pug']])
dogs_ind3 =dogs.set_index(['Breed', 'Owner'])
print(dogs_ind3)
print(dogs_ind3.loc[['Labrador', 'Pug']])
print(dogs_ind3.loc[[('Labrador', 'Colm'), ('Pug', 'Oisin')]])
print(dogs_ind3.sort_index())
print(dogs_ind3.sort_index(level=['Owner', 'Breed'], ascending=[True, False]))