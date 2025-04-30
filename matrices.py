import numpy as np

# simple 2d matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# element in row 2, column 3 (zero-indexed)
value = matrix[1][2]  # 6
# to get a row
row2 = matrix[1] # [4,5,6]
# to get a column
column3 = [row[2] for row in matrix] # [3,6,9] where row[2] represents the 3rd element in every row

# Limitations
# No native support for vectorised maths
# Manual loops are required for most operations, which are slow.

# Using NumPy

# 3x3 array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Array creation
zeros = np.zeros((2,5)) # all zeros, shape 2 x 5
ones  = np.ones((4, 4))        # all ones, shape 4×4
rand  = np.random.rand(3, 2)   # random floats in [0,1), shape 3×2
eye   = np.eye(5)              # 5×5 identity matrix
# print(eye) 
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# attributes
A.ndim   # 2
A.shape  # (3, 3)
A.dtype  # e.g. dtype('int64')
A.size   # 9

# Single element
A[1, 2]        # 6

# Slice rows 0–1, cols 1–2
sub = A[0:2, 1:3]  # array([[2, 3], [5, 6]])

# Select rows 0 and 2, columns 1 and 2
B = A[[0, 2], [1, 2]]  # array([2, 9])

# All elements > 5
mask = A > 5          # array([[False,...],[..]])
filtered = A[mask]    # array([6, 7, 8, 9])