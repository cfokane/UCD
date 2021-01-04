import numpy as np

continents = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'black'
}

for key, value in continents.items():
    print(key + '... ' + str(value))

import numpy as np
np_height = np.array([1.71, 1.73, 1.65, 1.83])
np_weight = np.array([80, 85, 67, 90])
bmi = np_weight / np_height ** 2
print(bmi)
for val in bmi :
    print(val)

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for country, capital in europe.items():
    print('the capital of ' + country + ' is ' + capital)