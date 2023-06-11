import pandas as pd
import numpy as np

diamonds = pd.read_csv('diamonds.csv')
print(diamonds)

# displaying the unique values of  a column
cut_list = diamonds['cut'].unique()
print(cut_list)

# Number of unique values
n = diamonds['cut'].nunique()
print(f'the number of unique values is {n}')

# examples of aggregation functions
# print(diamonds.mean())
# print(diamonds.agg('mean'))
print(diamonds[['carat', 'price']].agg(['mean', 'sum']))

diamonds.aggregate({"carat": ['max', 'min'],
                    "price": ['max', 'sum', 'mean'],
                    "depth": ['min', 'max']})

# ### Groupby
# The 3 Steps of a Groupby Process
# Any groupby process involves some combination of the following 3 steps:
# 1 - Splitting the original object into groups based on the defined categorical criteria.
# 2 - Applying a function to each group.
# 3 - Combining the results.

### 1. Splitting the Original DataFrame into Groups

grpcut = diamonds.groupby('cut')  # we are splitting the diamonds dataframe per cut
print(grpcut)

# grpcut is a GroupBy iterator object that contains group indexes and their respective contents
# groups and indices attributes of the groupby object
print(grpcut.indices)
print(grpcut.groups)  # numbers in the list are the row number.

# groupby iterator object also contains methods
print(grpcut.size())  # method to  display group sizes (how many rows).
print(grpcut.first())  # preview the result with the first or last entry for each group
print(grpcut.last())

print(grpcut.get_group('Good'))  # Get Specific  Group
print(grpcut.get_group('Good')[['carat', 'price']])  # Get Specific Group Columns (enables slicing)

# __Iterating over groups__
for name, group in grpcut:
    print(name)
    print(group)

# 2. Data Aggregation with groupby
# Aggregate functions in the Pandas package:
# count()  Number of non-null observations
# sum()  Sum of values
# mean()  Mean of values
# median()  Arithmetic median of values
# min()  Minimum
# max()  Maximum
# mode()  Mode
# std()  Standard deviation
# var()  Variance

# grpcut_mean = grpcut.mean()  # mean values for each numeric column by group.
# print(grpcut_mean)

grpcut_mean_price = grpcut['price'].mean()  # calculate mean for the 'price' column only
print(grpcut_mean_price)
print(type(grpcut_mean_price))  # cutgrp_mean_price is a Series

### Groupby multiple columns - count diamonds  per cut and color
grp_cut_color = diamonds.groupby(['cut', 'color'])
print(grp_cut_color.count())
print(grp_cut_color['price'].sum())

### Applying Multiple Aggregation Functions at Once using agg()
grp_cut_color[['price']].agg([np.sum, np.mean, np.std])


### Applying custom function
# The function return the number of diamonds with color 'D' for each group
def get_D_color(df):  # df is the DataFrame of each group
    return len(df[df["color"] == 'D'])


# Set the custom function as the parameter of apply()
print(grpcut.apply(get_D_color))

# ### Filtering: filter() , query()
# grpcut_mean = grpcut.mean()  # mean values for each numeric column by group.
print(grpcut.size())
# print(grpcut_mean)
print(grpcut['price'].filter(lambda x: x.mean() > 4400))
print(diamonds.query("color=='D'").groupby('cut').size())

# __Groupby and NaN__
df = pd.DataFrame(
    [(1, 'B', 121, 10.1, True),
     (2, 'C', 145, 5.5, False),
     (3, 'A', 345, 4.5, False),
     (4, 'A', 112, np.nan, True),
     (5, 'C', 105, 2.1, False),
     (6, np.nan, 435, 7.8, True),
     (7, np.nan, 521, np.nan, True),
     (8, 'B', 322, 8.7, True),
     (9, 'C', 213, 5.8, True),
     (10, 'B', 718, 9.1, False)],
    columns=['colA', 'colB', 'colC', 'colD', 'colE'])

print(df.groupby('colB')['colD'].sum())
print(df.groupby('colB', dropna=False)['colD'].sum())
df.fillna(-1).groupby('colB').sum()

print(df.groupby('colB').count())

print(df.groupby('colB', dropna=False).count())
