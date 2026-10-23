import numpy as np
import pandas as pd

data = pd.read_csv('./data/sample.csv')
df = pd.DataFrame(data)

print(df.head(4))

# Filtering: select rows based on one condition, then combine conditions with & and |.
print('-' * 45)
print('Filtering')
print('-' * 45)

df_condition_one = df['Stars'] >= 9
df_condition_two = df['Director'] >= 'James Burrows'

print(f'dataframe with first condition: \n{df[df_condition_one].head(4)}')
print(f'dataframe with second condition: \n{df[df_condition_two].head(4)}')

df_and = df[df_condition_one & df_condition_two]
df_or = df[df_condition_one | df_condition_two]

print(f'dataframe with AND condition: \n{df_and.head(4)}')
print(f'dataframe with OR condition: \n{df_or.head(4)}')

# Sorting: sort by a single column and by multiple columns using sort_values().
print('-' * 45)
print('Sorting')
print('-' * 45)

df_sorted_single = df.sort_values(by='Stars', ascending=False)

df_sorted_multiple = df.sort_values(by=['Stars', 'Director'], ascending=[False, True])

print(f'dataframe sorted by Stars (descending): \n{df_sorted_single.head(4)}')
print(f'dataframe sorted by Stars and Director: \n{df_sorted_multiple.head(4)}')

# Adding & removing columns: create a new calculated column, rename columns, and drop unwanted ones.\
print('-' * 45)
print('Adding & removing columns')
print('-' * 45)

df['Multi_Votes'] = df['Votes'] * 2 # adding calulated column to the dataframe
df.drop(columns=['Summary'], inplace=True) # removing column from the dataframe

print(df.head())

# Grouping & aggregation: use groupby() with sum(), mean(), count(), and agg() to summarise data.
print('-' * 45)
print('Grouping & aggregation')
print('-' * 45)

grouped_df = df.groupby('Season')[['Stars', 'Votes']]

print(f'grouped dataframe with sum: \n{grouped_df.sum().head(4)}')
print(f'grouped dataframe with mean: \n{grouped_df.mean().head(4)}')
print(f'grouped dataframe with count: \n{grouped_df.count().head(4)}')
print(f'grouped dataframe with agg: \n{grouped_df.agg(['sum', 'mean', 'count']).head(4)}')

# Merging & joining: merge two DataFrames on a common key with pd.merge() (inner, left, right, outer joins).
print('-' * 45)
print('Merging & joining')
print('-' * 45)

df_merged_inner = pd.merge(df,df, on='Year_of_prod', how='inner')
df_merged_left = pd.merge(df,df, on='Year_of_prod', how='left')
df_merged_right = pd.merge(df,df, on='Year_of_prod', how='right')
df_merged_outer = pd.merge(df,df, on='Year_of_prod', how='outer')

print(f'dataframe merged with inner join: \n{df_merged_inner.head(4)}')
print(f'dataframe merged with left join: \n{df_merged_left.head(4)}')
print(f'dataframe merged with right join: \n{df_merged_right.head(4)}')
print(f'dataframe merged with outer join: \n{df_merged_outer.head(4)}')

df_joined = df.join(df, lsuffix='_left', rsuffix='_right')

print(f'dataframe joined with inner join: \n{df_joined.head(4)}')

# Exercise: given a sales DataFrame, filter for sales > 500, group by region, compute total and average sales per region, and merge with a regions-info DataFrame.
print('-' * 45)
print('Exercise')
print('-' * 45)

# generate a sample sales DataFrame
rng = np.random.default_rng(42)
sales_df = pd.DataFrame({
	'Date': pd.date_range(start='2024-01-01', periods=50, freq='D'),
	'Product': rng.choice(['Laptop', 'Phone', 'Tablet', 'Headphones'], size=50),
	'Region': rng.choice(['North', 'South', 'East', 'West'], size=50),
	'Quantity': rng.integers(1, 11, size=50),
	'Unit_Price': rng.choice([49.99, 99.99, 199.99, 899.99], size=50),
})

# calculate total sales
sales_df['Sales'] = sales_df['Quantity'] * sales_df['Unit_Price']

# filter for sales > 500
filtered_sales_df = sales_df[sales_df['Sales'] > 500]

# group by region and compute total and average sales
grouped_sales_df = filtered_sales_df.groupby('Region').agg({'Sales': ['sum', 'mean']})

print(f'Filtered Sales DataFrame ({len(filtered_sales_df)} rows):\n{filtered_sales_df.head()}')
print(f'Grouped Sales DataFrame:\n{grouped_sales_df.head()}')
