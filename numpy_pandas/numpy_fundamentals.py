import numpy as np

# Indexing & slicing
index_slice = np.arange(20, dtype=int).reshape(4, 5)

print(index_slice)
print('Indexing single elements # ', index_slice[1, 2])
print('negative Indexing single elements # ', index_slice[-1, 1])

print ('Indexing rows # ', index_slice[2])
print ('negative Indexing rows # ', index_slice[-2])

print('Indexing columns # ', index_slice[:, 1])
print('negative Indexing columns # ', index_slice[:, -1])

print('Indexing sub-arrays # ', index_slice[1:2])
print('negative Indexing sub-arrays # ', index_slice[-2:-1])

# Boolean indexing
threshold = 7
print('Boolean indexing # ', index_slice[index_slice > threshold])

# Fancy indexing
fancy_index = np.array([2, 3])
print('fancy indexing # ', index_slice[fancy_index])

# Reshaping
reshaped = np.arange(12).reshape(3, 4)
ravel = reshaped.ravel()
flattened = reshaped.flatten()
transposed = reshaped.transpose()

print('reshaped array # ', reshaped)
print('raveled array # ', ravel)
print('flattened array # ', flattened)
print('transposed array # ', transposed)

# Stacking & splitting
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])

# Stacking
h_stacked = np.hstack((arr_1, arr_2))
v_stacked = np.vstack((arr_1, arr_2))

print('Horizontally stacked array # ', h_stacked)
print('Vertically stacked array # \n', v_stacked)

# concatenation
concatenated = np.concatenate((arr_1, arr_2))

print('Concatenated array # ', concatenated)

# splitting
split_arr = np.split(concatenated, 2)

print('Split arrays # ', split_arr)

# Element-wise operations
arr_a = np.random.rand(3, 3)
arr_b = np.random.rand(3, 3)

print('Element-wise addition # \n', arr_a + arr_b)
print('Element-wise subtraction # \n', arr_a - arr_b)
print('Element-wise multiplication # \n', arr_a * arr_b)
print('Element-wise division # \n', arr_a / arr_b)

# Broadcasting
_1d = np.array([1, 2, 3])
_2d = np.random.rand(3, 3)

print('Broadcasting # \n', _1d + _2d)

# Aggregation functions
arr = np.random.rand(4, 4)
print('Sum of all elements # ', np.sum(arr, axis=1))
print('Mean of all elements # ', np.mean(arr, axis=0))
print('Standard deviation of all elements # ', np.std(arr, axis=1))
print('Minimum of all elements # ', np.min(arr))
print('Maximum of all elements # ', np.max(arr))
print('argmin of all elements # ', np.argmin(arr))
print('argmax of all elements # ', np.argmax(arr))

# Universal functions (ufuncs)
arr = np.array([1, 2, 3, 4, 5])

print('Square root # ', np.sqrt(arr))
print('Exponential # ', np.exp(arr))
print('Logarithm # ', np.log(arr))
print('Sine # ', np.sin(arr))

# Random module
rng = np.random.default_rng(seed=42)

# random integers
rand_int = rng.integers(low=0, high=10, size=(3, 3))

# random floats
rand_float = rng.random((3, 3))

# random normal distribution
rand_normal = rng.normal(loc=0.0, scale=1.0, size=(3, 3))

print('Random integers # \n', rand_int)
print('Random floats # \n', rand_float) 
print('Random normal distribution # \n', rand_normal)

# Exercise
ex = rng.integers(low=1, high=101, size=(5, 5))

row_sums = ex.sum(axis=1)
row_index = np.argmax(row_sums)
max_row = row_sums[row_index]

ex[ex < 50] = 0

print('Exercise result:\n', ex)