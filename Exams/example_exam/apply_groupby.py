import pandas as pd
import numpy as np
"""

# Quick examples of pandas apply() function
def add_3(x):
    return x + 3


data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("Create DataFrame:\n", df)
print()

# Using Dataframe.apply() – apply function to all the values
df2 = df.apply(add_3)
print(df2)
print()

# Apply to columns
df2 = df
df2["B"] = df2["B"].apply(add_3)
print(df2)
print()

df2 = df
# Apply to multiple columns
df2[['A', 'B']] = df2[['A', 'B']].apply(add_3)
print(df2)
print()

# Apply a lambda function to each column
df2 = df2.apply(lambda x: x + 10)
print(df2)
print()

print(df)
# Using Dataframe.apply() and lambda function
df["A"] = df["A"].apply(lambda x: x - 2)
print(df)
print()

# applying numpy function
df['A'] = df['A'].apply(np.square)
print(df)
print()


# Another example
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# define a function to apply to the salary column
def salary_increase(salary):
    return salary * 1.1


print(df)
# apply the function to the salary column using apply()
df['salary'] = df['salary'].apply(salary_increase)
print(df)


# Apply to rows
# Function to add
def add_values(row):
    return row['A'] + row['B'] + row['C']


# Create a dictionary with three fields each
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]}
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# Apply the user-defined function to every row
df['add'] = df.apply(add_values, axis=1)

print('\nAfter Applying Function: ')
# Print the new DataFrame
print(df)


# using lambda
# Function to add

def add(a, b, c):
    return a + b + c


# create a dictionary with three fields each
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df['add'] = df.apply(lambda row: add(row['A'], row['B'], row['C']), axis=1)

print('\nAfter Applying Function: ')
# printing the new dataframe
print(df)


# Another example
def normalize(x, y):
    x_new = ((x - np.mean([x, y])) /
             (max(x, y) - min(x, y)))
    print(x_new)
    return x_new


# create a dictionary with three fields each
data = {
    'X': [1, 2, 3],
    'Y': [45, 65, 89]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df['X'] = df.apply(lambda row: normalize(row['X'],
                                         row['Y']), axis=1)

print('\nNormalized:')
print(df)

# Example of the difference between axis=0 and axis=1
data = [(3, 5, 7), (2, 4, 6), (5, 8, 9)]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print("Create DataFrame:\n", df)
print()

df1 = df.apply(sum)
print("Apply sum with axis=0:\n", df1)

df2 = df.apply(sum, axis=1)
print("Apply sum with axis=1:\n", df2)

"""
#  Example of working with groupby objects
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar'],
                   'B': [1, 2, 3, 4, 5, 6],
                   'C': [2.0, 5., 8., 1., 2., 9.]})
print(df)
print()
grouped = df.groupby('A')
#print(grouped)
#print(grouped.groups)
#print(grouped.get_group('foo'))

g = grouped.mean()
#print(g)
#print(g.index)
#print(g)
g.reset_index(inplace=True)
#print(g)

#print(grouped.groups)
#print()
#print(grouped.get_group('foo'))

# the 2 lines above are the same
print(grouped.filter(lambda x: x['B'].mean() > 3.))
print(df.groupby('A').filter(lambda x: x['B'].mean() > 3.))
# Another way to find the rows with a group mean greater than 3
grouped_3 = df.groupby('A')['B'].mean()
print()

print(grouped_3)
print()
print(grouped_3.index)
print()
x = list(grouped_3[grouped_3 > 3.].index)
print(x)
print(df[df['A'] == x[0]])


# Examples of apply method
def fun(num):
    if num <= 50:
        return "Low"
    elif 50 < num <= 70:
        return "Normal"
    else:
        return "High"


# Create a series of 20 random integers between 10 and 100
s = pd.Series(np.random.randint(10, 100, 20))
print(s)
s2 = s.apply(fun)
print(s2)


s3 = s[s > 30].apply(lambda x: x + 10)
print(s3)

