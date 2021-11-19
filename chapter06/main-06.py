from numpy import *
from numpy.linalg import *

A = array([[1, 2, 3], [22, 32, 42], [55, 66, 100]])  # Array of arrays
print('A =', A)

b = array([1, 2, 3])

x = solve(A, b)
print(x)

print(dot(A, x))

# x = y A^-1 b
print(dot(inv(A), A))
print('x = ', multiply(inv(A), b))

