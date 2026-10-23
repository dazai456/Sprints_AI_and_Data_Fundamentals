import numpy as np
import pandas as pd

data = pd.read_csv('./data/sample.csv')

df = pd.DataFrame(data)

print(df.head(4))

# Descriptive statistics: compute mean, median, mode, variance, and standard deviation for numerical columns.
print('-' * 45)
print('Descriptive statistics')
print('-' * 45)

df_num_col = df.select_dtypes(include=['float64', 'int64'])

print(f'\ndf mean # \n{df_num_col.mean()}')
print(f'\ndf median # \n{df_num_col.median()}')
print(f'\ndf mode # \n{df_num_col.mode()}')
print(f'\ndf variance # \n{df_num_col.var()}')
print(f'\ndf standard deviation # \n{df_num_col.std()}')

# Value counts: use value_counts() to summarise categorical columns.
print('-' * 45)
print('Value counts')
print('-' * 45)

df_cat_col = df[['Year_of_prod', 'Season', 'Director']]
print(df_cat_col.head())
print(f'\n df value count \n{df_cat_col.value_counts()}')

# Correlation: generate a correlation matrix with corr() and interpret the results.
print('-' * 45)
print('Correlation')
print('-' * 45)

corr = df_num_col.corr()
print(corr)

# Pivot tables: create a pivot table with pd.pivot_table() using different aggregation functions.
print('-' * 45)
print('Pivot table')
print('-' * 45)

pivot = pd.pivot_table(
    df,
    index=['Season', 'Director'],          # Rows will be Seasons
    # columns='Director',      # Columns will be Directors
    values='Stars',          # We are analyzing the 'Stars' column
    aggfunc=['mean', 'min', 'max']           # Find the average rating
)

print(pivot.head(5))

# Cross-tabulation: use pd.crosstab() to compare two categorical variables.
print('-' * 45)
print('Cross-tabulation')
print('-' * 45)

df_cross = pd.crosstab(df_cat_col['Director'], df_cat_col['Year_of_prod'])

print(df_cross)

# Apply & map: use apply() with a custom function and map() to transform a column.
print('-' * 45)
print('Apply & map')
print('-' * 45)

# Apply
df['Title Len'] = df['Episode_Title'].apply(lambda title: len(title))

print(df['Title Len'].head(5))

# Mapping
season_names = {i: f'Season_{number}' for i, number in enumerate(
    ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'],
    start=1,
)}

df['Season_Name'] = df['Season'].map(season_names)

print(df['Season_Name'].head(5))

# Time-series basics: parse date columns with pd.to_datetime(), set a DatetimeIndex, and resample data by month.

# Exercise: load a dataset, produce descriptive stats, build a pivot table summarising average values by category, and create a simple line chart of a time-series column using df.plot().