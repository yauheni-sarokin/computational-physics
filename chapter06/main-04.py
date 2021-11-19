# shaping array

import numpy as np

array = np.arange(12)
print(array)

array = array.reshape((3, 4))
print(array)

print(array.shape)
print(array.ndim)

print(array.T)

print(array[:2:])
