from numpy import *
from numpy.linalg import eig

# A = array([[1, 2, 3], [22, 32, 42], [55, 66, 100]])  # Array of arrays
I = array([[2. / 3, -1. / 4], [-1. / 4, 2. / 3]])
print('I = \n', I)
Es, evectors = eig(I)  # Solves eigenvalue problem
print('Eigenvalues = ', Es, '\n Eigenvector Matrix =\n', evectors)

Vec = array([evectors[0, 0], evectors[1, 0]])
LHS = dot(I, Vec)
RHS = Es[0] * Vec
print('LHS - RHS =', LHS - RHS)

