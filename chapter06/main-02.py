# matrix

from vpython import *
from numpy import array

vector1 = array([1, 2, 3, 4, 5])
print('vector1 ==', vector1)

vector2 = vector1 + vector1
print('vector2 ==', vector2)

matrix1 = array(([0, 1], [1, 3]))
print(matrix1)

matrix2 = matrix1 * matrix1
print(matrix2)