# Matrix-vector multiplication and Matrix multiplication

import numpy as np 

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[2], [4]])

# Matrix-vector multiplication
C = A.dot(B)

# Matrix multiplication
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
B = np.array([[2, 7], [1, 2], [3, 6]])
C = A.dot(B)