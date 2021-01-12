import numpy as np
import pandas as pd

dogs=pd.read_csv('dogs.csv', index_col=0)
print(dogs)

dogs_srt = dogs.sort_index()
print(dogs_srt)
print(dogs_srt.loc["Coco":"Milo"])


# Subset in both directions at once
print(dogs_srt.loc[("Dump", "Doberman"):("Milo", "Pug"), "DOB":"Colour"])