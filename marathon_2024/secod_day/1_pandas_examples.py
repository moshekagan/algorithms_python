import pandas as pd

def my_print(*args):
    print(*args, end='\n\n--------------------------------------------\n\n')

# Creating a Series
series = pd.Series([1, 2, 3, 4, 5])
my_print(series)

# Series Methods
my_print(series.values)
my_print(series.index)
my_print(series.dtype)
my_print(series.mean())
my_print(series.std())

# Creating a DataFrame
data = {'Name': ['John', "Yossi", 'Jane', 'Mike', 'Alice'], 'Age': [23, 25, 25, 30, 22], "Grads": [100, 95, 90, 80, 70]}
df = pd.DataFrame(data)
my_print(df)

# DataFrame Methods
my_print(df.head())
my_print(df.tail())
my_print(df.info())
my_print(df.shape)
my_print("rows", df.shape[0])
my_print("columns", df.shape[1])
my_print(df.describe())
my_print(df.columns)
my_print(df.index)

# Indexing and Selecting Data
my_print(df.iloc[0])  # First row
my_print(df.loc[0])  # First row

df = df.set_index('Name')
my_print(df)

df_sorted = df.sort_index()
my_print(df_sorted)

df_reset = df.reset_index()
my_print(df_reset)

# Reading Data
df_from_csv = pd.read_csv('sample.csv')
my_print(df_from_csv)

# Filtering Data
filter_data = df['Age'] > 25
# filter_data = [False, False, True, False]
filtered_df = df[filter_data]
my_print(filtered_df)


filtered_selected_df = df.loc[df['Age'] > 25, ['Grads']]
my_print(filtered_selected_df)

query_df = df.query('Age > 25')
my_print(query_df)


# Checkin membership
is_in_list = series.isin([1, 2])
my_print(is_in_list)

string_series = pd.Series(['apple', 'banana', 'cherry'])
contains_substring = string_series.str.contains('a')
my_print(string_series[contains_substring])
my_print(contains_substring)


# Rename columns
df_renamed = df.rename(columns={'Age': 'Years'})
my_print(df_renamed)

# Drop data
# row
df_dropped = df.drop(['John'])
my_print(df_dropped)

# column
df_dropped_column = df.drop(['Age'], axis=1)
my_print(df_dropped_column)

# Grouping Data
grouped = df.groupby('Age').sum(["Age"])
my_print(grouped)

df_with_nan = pd.DataFrame({'Name': ['John', 'Jane', 'Mike', None], 'Age': [23, 25, 30, None]})
grouped_with_nan = df_with_nan.groupby('Age', dropna=False).sum()
my_print(grouped_with_nan)


# Merging data
# Create two sample DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['John', 'Jane', 'Mike', 'Alice']})
df2 = pd.DataFrame({'ID': [2, 3, 4, 5], 'Age': [25, 30, 35, 40]})

# Merge the DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID')
my_print(merged_df)
