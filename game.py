import numpy as np

np.random.seed(123)
coin=np.random.randint(0, 2)
print(coin)
if coin == 0 :
    print('heads')
else :
    print ('tails')
