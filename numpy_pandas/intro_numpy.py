import numpy as np

# Install NumPy and import it as np. Print the installed version.
print(np.__version__)

# Create a 1-D array from a Python list, a 2-D array from nested lists, and a 3-D array
py_list = [1, 9, 8, 2, 3, 4, 5]

py_3d_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

np_arr = np.array(py_list)

np_3d_arr = np.array(py_3d_list)

# Use convenience constructors
np_zeros = np.zeros((3, 4))

np_ones = np.ones((2, 3))

np_arrange = np.arange(1, 10)

np_linspace = np.linspace(0, 12, 4)

np_eye = np.eye(3, 5)

print('np zeros: \n', np_zeros)
print('np ones: \n', np_ones)
print('np arrange: \n', np_arrange)
print('np linspace: \n', np_linspace)
print('np eye: \n', np_eye)

# Inspect array attributes
att = np.ones((5,5))

print('shape # ', att.shape)
print('dtype # ', att.dtype)
print('size # ', att.size)
print('ndim # ', att.ndim)
print('itemsize # ', att.itemsize)

# Timing comparison for NumPy vs Python lists
import time

n = 1000000

# Python list sum
start = time.time()
arr = list(range(n))
_sum = 0

for i in arr:
    _sum += i

print('Python list time: ', time.time() - start)

# numpy array sum
start = time.time()
np_arr = np.arange(n)
np_sum = np.sum(np_arr)

print('NumPy array time: ', time.time() - start)
