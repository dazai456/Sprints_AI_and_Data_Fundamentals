import numpy as np

# Compute the dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
at_op = a @ b

print('dot product:', dot_product)
print('using @ operator:', at_op)

# Perform matrix multiplication
a_matrix = np.array([[1, 2], [3, 4]])
b_matrix = np.array([[5, 6], [7, 8]])

matrix_product = np.matmul(a_matrix, b_matrix)

print('matrix product:\n', matrix_product)

# Calculate the determinant and inverse
determinant = np.linalg.det(a_matrix)
inverse = np.linalg.inv(a_matrix)

print('determinant:', determinant)
print('inverse:\n', inverse)

# Find the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(a_matrix)

print('eigenvalues:', eigenvalues)
print('eigenvectors:\n', eigenvectors)

# Solve a system of linear equations (Ax = b)
A = np.array([[2, 1], [1, 1]])
b = np.array([3, 2])
x = np.linalg.solve(A, b)

print('solution:', x)

# Compute the norm of a vector
norm = np.linalg.norm(a)
rank = np.linalg.matrix_rank(a)

print('norm of vector a:', norm)
print('rank of matrix a:', rank)

# Exercise

prod_prices = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
stores = np.array([1, 2, 3])

x = np.linalg.solve(prod_prices, stores)
print('solution:', x)