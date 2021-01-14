import pandas as pd
S_E = pd.read_csv('covid-stringency-index.csv', index_col=0)
E_U = pd.read_csv('states.csv', index_col=0)
#print(S_E.head(5))
#print(E_U.head(10))
#for val in S_E :
#    print(val)
#print(S_E.head(3))
#print(S_E.info())
#print(S_E.describe())

#print(S_E.shape)
#print(S_E.columns)
#print(E_U.columns)
#print(S_E.index)
#print(E_U.index)
EU=(pd.concat([S_E, E_U], sort=True))
print(EU.head)