import numpy as np

# Structured arrays
print('\n' + '-' * 20)
print('Structured arrays')
print('-' * 20)

schema = [
    ('name', 'S20'),    # 20-character string
    ('age', 'i4'),      # 32-bit integer
    ('score', 'f8')    # 64-bit float
]

str_arr = np.array([
    ('Dazai', 25, 85.5),
    ('Luffy', 30, 92.0),
    ('Naruto', 22, 78.0)
], dtype=schema)

print(str_arr)

# Accessing fields in a structured array
print(str_arr['name'])
print(str_arr[['age', 'score']])

# Memory layout
print('\n' + '-' * 20)
print('Memory layout')
print('-' * 20)

mem_arr = np.array([[1, 2, 3], [4, 5, 6]])
print('2D array strides # ', mem_arr.strides)
print('Is C-contiguous:', mem_arr.flags['C_CONTIGUOUS'])


trans = mem_arr.T
print('Transposed array strides # ', trans.strides)
print('Is C-contiguous:', trans.flags['C_CONTIGUOUS'])


cont_arr = np.ascontiguousarray(mem_arr)  # Convert to contiguous array
print('Contiguous array strides # ', cont_arr.strides)
print('Is C-contiguous:', cont_arr.flags['C_CONTIGUOUS'])


# Views vs copies
print('\n' + '-' * 20)
print('Views vs copies')
print('-' * 20)

org_arr = np.array([1, 2, 3, 4, 5])

print('Original array:', org_arr)

# creating a view of the original array
slice_view = org_arr[1:4]
print('Slice view:', slice_view)

# modifying the view
slice_view[0] = 20

print('Modified slice view:', slice_view)
print('Original array after modifying the view:', org_arr)


# copying the original array
slice_view[0] = 2  # Resetting the value to original for clarity
print('original array:', org_arr)

fancy_indexing = org_arr[[0, 2, 4]]
print('Fancy indexing result:', fancy_indexing)

# modifying the fancy indexing result
fancy_indexing[0] = 10

print('Modified fancy indexing result:', fancy_indexing)
print('Original array after modifying fancy indexing result:', org_arr)

# Vectorise custom functions
print('\n' + '-' * 20)
print('Vectorised custom functions')
print('-' * 20)

import datetime

# Define a custom function
def custom_function(x):
    return x ** 2 + 2 * x + 1

# Vectorise the custom function
vectorised_function = np.vectorize(custom_function)

# Apply the vectorised function to an array
start = datetime.datetime.now()

arr = np.array([1, 2, 3, 4, 5])
result = vectorised_function(arr)

print('Vectorised function result:', result)
print('Time taken for vectorised function:', datetime.datetime.now() - start)

# numpy vectorize
start = datetime.datetime.now()

arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 2, arr ** 2 + 2 * arr + 1, arr)

print('NumPy vectorize result:', result)
print('Time taken for NumPy vectorize:', datetime.datetime.now() - start)

# np.where() & np.select()
print('\n' + '-' * 20)
print('np.where() & np.select()')
print('-' * 20)

my_array = np.array([1, 2, 3, 4, 5])

# Using np.where() to apply a condition

where_result = np.where(my_array > 2, my_array ** 2 + 2 * my_array + 1, my_array)

print('np.where() result:', where_result)

# Using np.select() to apply multiple conditions
conditions = [my_array < 2, my_array >= 2]
choices = [my_array * 2, my_array ** 2 + 2 * my_array + 1]

select_result = np.select(conditions, choices)
print('np.select() result:', select_result)

# Exercise
print('\n' + '-' * 20)
print('Exercise')
print('-' * 20)

# generate a 1000 × 1000 random matrix
rand_matrix = np.random.rand(1000, 1000)

min_val = rand_matrix.min(axis=0) 
max_val = rand_matrix.max(axis=0)  

# nornalize the matrix
norm_matrix = (rand_matrix - min_val) / (max_val - min_val)

# verifying the normalization
norm_min = norm_matrix.min(axis=0)
norm_max = norm_matrix.max(axis=0)

print(norm_min[1:10])
print(norm_max[1:10])
