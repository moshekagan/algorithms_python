# Pandas
```python
import pandas as pd
```

### List of common functions:
- `pd.Series()`: Creates a pandas Series object.
- `pd.DataFrame()`: Creates a pandas DataFrame object.
- `pd.Series.values`: Returns the values of a Series object.
- `pd.Series.index`: Returns the index of a Series object.
- `pd.Series.dtype`: Returns the data type of a Series object.
- `pd.Series.mean()`: Calculates the mean of a Series object.
- `pd.Series.std()`: Calculates the standard deviation of a Series object.
- `pd.DataFrame.head()`: Returns the first n rows of a DataFrame.
- `pd.DataFrame.tail()`: Returns the last n rows of a DataFrame.
- `pd.DataFrame.info()`: Provides information about a DataFrame.
- `pd.DataFrame.shape`: Returns the number of rows and columns of a DataFrame.
- `pd.DataFrame.describe()`: Generates descriptive statistics of a DataFrame.
- `pd.DataFrame.columns`: Returns the column labels of a DataFrame.
- `pd.DataFrame.index`: Returns the index labels of a DataFrame.
- `pd.DataFrame.iloc[]`: Accesses DataFrame elements by index-based location.
- `pd.DataFrame.loc[]`: Accesses DataFrame elements by label-based location.
- `pd.DataFrame.set_index()`: Sets a column as the DataFrame's index.
- `pd.DataFrame.sort_index()`: Sorts the DataFrame by index.
- `pd.DataFrame.reset_index()`: Resets the DataFrame index to default.
- `pd.read_csv()`: Reads a CSV file into a DataFrame.
- `pd.DataFrame[condition]`: Filters DataFrame rows based on a condition.
- `pd.DataFrame.loc[condition, columns]`: Filters DataFrame rows and selects specific columns based on a condition.
- `pd.DataFrame.query()`: Filters DataFrame rows based on a query string.
- `pd.Series.isin()`: Checks if elements in a Series are present in a list of values.
- `pd.Series.str.contains()`: Checks if string elements in a Series contain a specific substring.
- `pd.DataFrame.rename()`: Renames columns of a DataFrame.
- `pd.DataFrame.columns`: Returns the column labels of a DataFrame.
- `pd.DataFrame.drop()`: Removes columns from a DataFrame.
- `pd.DataFrame.loc[row, column]`: Accesses DataFrame elements by label-based location.
- `pd.DataFrame.apply()`: Applies a function to a DataFrame or Series.
- `pd.DataFrame.apply(lambda)`: Applies a lambda function to a DataFrame or Series.
- `pd.Series.isna()`: Checks for missing values (NaN) in a Series.
- `pd.Series.fillna()`: Fills missing values in a Series with specified values.
- `pd.DataFrame.dropna()`: Drops rows or columns with missing values from a DataFrame.
- `pd.DataFrame.isna()`: Checks for missing values (NaN) in a DataFrame.
- `pd.DataFrame.shape`: Returns the number of rows and columns of a DataFrame.
- `pd.DataFrame.loc[:, condition]`: Filters DataFrame columns based on a condition.
- `pd.DataFrame.isna().sum()`: Calculates the sum of missing values in each column of a DataFrame.
- `pd.DataFrame.loc[:, condition]`: Filters DataFrame columns based on a condition.
- `pd.Series.value_counts`: is a pandas function that returns a count of unique values in a Series, providing a summary of the frequency distribution of values.
- `pd.Series.nlargest`: is a pandas function that returns the n largest values from a Series, allowing you to quickly identify the top values based on their magnitude or order.


### More
- `pd.read_csv('diamonds.csv')`: Reads a CSV file and returns a DataFrame.
- `df['column_name'].unique()`: Returns an array of unique values in a column.
- `df['column_name'].nunique()`: Returns the number of unique values in a column.
- `df.mean()`: Computes the mean of each column in the DataFrame.
- `df.agg('mean')`: Applies the 'mean' aggregation function to each column in the DataFrame.
- `df[['col1', 'col2']].agg(['mean', 'sum'])`: Applies multiple aggregation functions to specific columns in the DataFrame.
- `df.aggregate({"col1": ['func1', 'func2'], "col2": ['func3', 'func4']})`: Aggregates specific columns with multiple aggregation functions.
- `df.groupby('column_name')`: Groups the DataFrame by a column.
- `grouped.size()`: Returns the group sizes.
- `grouped.first()`: Returns the first entry for each group.
- `grouped.last()`: Returns the last entry for each group.
- `grouped.get_group('group_name')`: Returns a specific group from the groupby object.
- `for name, group in grouped: ...`: Iterates over groups and performs actions on each group.
- `grouped.mean()`: Computes the mean values for each numeric column by group.
- `grouped['column_name'].function()`: Applies an aggregation function to a specific column in the grouped DataFrame.
- `df.groupby(['col1', 'col2'])`: Groups the DataFrame by multiple columns.
- `grouped.count()`: Counts the occurrences of each group in the grouped DataFrame.
- `grouped['column_name'].function()`: Applies an aggregation function to a specific column in the grouped DataFrame.
- `df.groupby('column_name').apply(custom_function)`: Applies a custom function to each group.
- `df['column_name'].filter(lambda x: condition)`: Filters rows based on a condition.
- `df.query("condition")`: Filters rows based on a query string.
- `df.groupby('column_name')['column_name'].sum()`: Calculates the sum of a column for each group.
- `df.groupby('column_name').count()`: Counts the occurrences of each group in the DataFrame.
- `df.groupby('column_name', dropna=False)['column_name'].sum()`: Groups the DataFrame by a column, including NaN values.
- `df.fillna(value).groupby('column_name').sum()`: Fills missing values and groups the DataFrame by a column.
- `df.groupby('column_name').count()`: Counts the occurrences of each group in the DataFrame, including NaN values.
- `pd.merge`  
    - The merge function in pandas is used to combine two or more DataFrames based on a common column or index. It allows you to perform database-style joins, similar to the SQL JOIN operation.
    - ```merged_df = pd.merge(left_df, right_df, on='common_column')```
    - `left_df` and `right_df` are the DataFrames to be merged.
    - `on='common_column'` specifies the common column on which the merge operation will be performed. It can also be a list of column names if multiple columns are involved.
    - By default, `merge` performs an inner join, which means only the matching rows between the DataFrames will be included in the resulting DataFrame.
    - If you want to perform a different type of join, you can specify the `how` parameter. Some common options for `how` include `'inner'` (default), `'left'`, `'right'`, and `'outer'`.
    - In addition to the `on` parameter, you can also use the `left_on` and `right_on` parameters to specify different column names in the left and right DataFrames for the merge operation.
    - If you want to merge based on the DataFrame index instead of a column, you can use the `left_index=True` and/or `right_index=True` parameters.      
  ```.python
  # Create two sample DataFrames
  df1 = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['John', 'Jane', 'Mike', 'Alice']})
  df2 = pd.DataFrame({'ID': [2, 3, 4, 5], 'Age': [25, 30, 35, 40]})
  
  # Merge the DataFrames on the 'ID' column
  merged_df = pd.merge(df1, df2, on='ID')
  
  print(merged_df)
  ```
  Output:
  ```   
     ID  Name  Age
  0   2  Jane   25
  1   3  Mike   30
  2   4  Alice  35
  ```
