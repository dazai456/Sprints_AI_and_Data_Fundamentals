'''
what Pandas is and why it is the go-to library for tabular data in Python
=>
    Pandas is a powerful, open-source data manipulation and analysis library built on top of Python
    it has become the go-to library for working with tabular data due to its ease of use, performance, and flexibility. 
    It provides two primary data structures: Series (1-dimensional) and DataFrame (2-dimensional), which allow for efficient handling of structured data.
'''

import numpy
import pandas as pd

# Create a Series from a list and from a dictionary. Access elements by index label and position.
print('-' * 45)
print('Creating Series from List and Dictionary')
print('-' * 45)
ls = [1, 2, 3, 4, 5]
dict = {'a': 1, 'b': 2, 'c': 3}

ls_series = pd.Series(ls)
dict_series = pd.Series(dict)

print(f"List Series: \n{ls_series}")

print(f"\nDictionary Series: \n{dict_series}")

# Create a DataFrame from a dictionary of lists, from a list of dictionaries, and from a NumPy array.
import numpy as np

print('-' * 45)
print('Creating DataFrame from Dictionary of Lists and List of Dictionaries and from a NumPy array.')
print('-' * 45)

dict_of_ls = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
list_of_dicts = [{'a': 1, 'b': 4, 'c': 7}, {'a': 2, 'b': 5, 'c': 8}, {'a': 3, 'b': 6, 'c': 9}]
np_list = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

df_dict_of_ls = pd.DataFrame(dict_of_ls)
df_list_of_dicts = pd.DataFrame(list_of_dicts)
df_np = pd.DataFrame(np_list)

print(f"DataFrame from Dictionary of Lists: \n{df_dict_of_ls}")
print(f"\nDataFrame from List of Dictionaries: \n{df_list_of_dicts}")
print(f"\nDataFrame from NumPy array: \n{df_np}")


# Read data from a CSV file with pd.read_csv() and display the first/last rows with head()/tail().
print('-' * 45)
print('Reading CSV file into a DataFrame')
print('-' * 45)
data = pd.read_csv('./data/sample.csv')
df_csv = pd.DataFrame(data)

print(f"\nfirst rows of CSV DataFrame: \n{df_csv.head()}")
print(f"\nlast rows of CSV DataFrame: \n{df_csv.tail()}")


# Inspect the DataFrame: info(), describe(), dtypes, shape, columns, and index.
print('-' * 45)
print('Inspecting DataFrame')
print('-' * 45)

print('dataframe info: \n', df_csv.info)
print('dataframe describe: \n', df_csv.describe())
print('dataframe data types: \n', df_csv.dtypes)
print('dataframe shape:', df_csv.shape)
print('dataframe columns:', df_csv.columns)
print('dataframe index:', df_csv.index)

# Select columns by name, select rows with .loc[] (label) and .iloc[] (position).
print('-' * 45)
print('Selecting columns and rows')
print('-' * 45)

print(f'select by name # \n{df_csv["Season"]}')
print(f'select by .loc[] # \n{df_csv.loc[0]}')
print(f'select by .iloc[] # \n{df_csv.iloc[2]}')

# Handle missing data: use isnull(), dropna(), and fillna() on a DataFrame with intentional NaN values.
print('-' * 45)
print('Handling missing data')
print('-' * 45)

na_values = {'Season': [2020, 2021, 2022, 2026], 'Team': ['A', 'B', None, 'D'], 'Wins': [10, 12, 15, 20], 'Losses': [5, 10, None, 2], 'Draws': [None, 2, 3, 4]}
df_na = pd.DataFrame(na_values)

print(f'DataFrame with NaN values: \n{df_na}')
df_na.dropna(inplace=True)
df_na.fillna(0, inplace=True)

print(f'\nDataFrame after dropping NaN values: \n{df_na}')