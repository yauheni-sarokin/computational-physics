# complex numbers in array
from numpy import *

c = array([[1, complex(2, 2)], [complex(3, 2), 4]], dtype=complex)
print(c)

# multiplication of mitrices
matrix1 = array([[0, 1], [1, 3]])
print(matrix1)

matrix2 = dot(matrix1, matrix1)
print(matrix2)
