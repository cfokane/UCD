import numpy as np

np.random.seed(122)
coin = np.random.randint(0, 2)
print(coin)
if coin == 0:
    print ('tails')
else:
    print ('heads')

np.random.seed(123)
print(np.random.rand())

import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

import numpy as np
np.random.seed(123)
step = 50

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

