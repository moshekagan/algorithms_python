import pandas as pd
import numpy as np
# pandas Series - a hashable vector
# assign values to a series of indexes
letters = [chr(i) for i in range(97,123)]
a=np.random.normal(loc=0.5, scale = 1, size=len(letters))
s = pd.Series(a,index=letters,dtype = 'int64')
print(s.values)
print(s.index)
print(s.dtype)
# assigning series from dictionary
# dictionary keys become series' indexes
d = {'a':1,'b':10,'c':100}
s_d = pd.Series(d,dtype = 'int32')

# Series slicing is a hybrid of 1Darray slicing and dictionary slicing
# index slicing [from:to(not including):step]
print(s[2:10:2])
print(s[:-3])
print(s[::-1])
# key slicing by index names is similar to dictionary key slicing
# but more powerful, because of indexation
print(s['d'])
print(s['d':'k'])
print(s['d':'k'])
print(s['d':'k':3])
print(f"is 'k' in s? {'k' in s}")

# basic mathematical operations is enabled:
print(s.mean(),s.std())
print(s*s)
print(5*s)

# filtering is enabled like in numpy arrays
s[abs(s)>abs(s).mean()]
# use s.index to find positive filter index-locations (instead of np.where)
s.index[abs(s)>abs(s).mean()]
# also true for complex conditions
s[(s>-0.5)&(s<0.5)]
s.index[(s>-0.5)&(s<0.5)]

# pandas DataFrame
# a 2D labeled structure: each cell has index and column labels
df = pd.DataFrame()
print(df)
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, 9, 9, 20, 14.5, 7, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
data_exam = pd.DataFrame(exam_data)
print(data_exam)
print(type(data_exam))
# Creating a Dataframe from a list of lists

data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

# Creating DataFrame from csv file
data_csv = pd.read_csv('diamonds.csv')
print(data_csv)
# Display 10  first lines
print(data_csv.head(10))
# Display 10  last lines
print(data_csv.tail(10))
# Display data info
print(data_csv.info())
# Display  shape - number of rows and columns (attribute, not a function)
print(data_csv.shape)
# Describe numeric data
print(data_csv.describe())
# Display the columns' names (attribute, not a function)
print(data_csv.columns)
# Display the data's indexes (attribute, not a function)
print(data_csv.index)

##  Data Selection:
# column slicing
# Getting one column
print(data_csv['cut']  )
print(type(data_csv['cut']))
print(data_csv['cut'].value_counts() )
print(data_csv['cut'].unique())  # column's unique values
print(set(data_csv['cut']))  # column's unique values
print(data_csv['cut'].nunique() ) # number of unique values in a column

# Getting more than one column
print(data_csv[['cut', 'price']])  # column names are in a list

# Slicing by index/column position using df.iloc[]
# df.iloc[from:to(not including):step,from:to(not including):step]
# relates to --> df.iloc[row slicing,column slicing]
# defaults:
# df.iloc[0:df.shape[0]:1,0:df.shape[1]:1]

print(data_csv.iloc[0])   # first row of the dataframe
print(data_csv.iloc[[0, 2]])    # first and third rows of the dataframe
print(data_csv.iloc[[0, 1], [1, 4]])
print(data_csv.iloc[0:2, 1:3])     # slicing

# another df example
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, 9, 9, 20, 14.5, 7, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data_dict = pd.DataFrame(exam_data, index=labels)
print(data_dict)
print(data_dict.index)

# Slicing by index/column label using df.loc[]
# df.iloc[from rowname:to rowname(not including):step,from colname:to colname(not including):step]
# relates to --> df.iloc[row slicing,column slicing]

print(data_dict.loc['a'])
print(data_dict.loc[['a', 'c']])
print(data_dict.loc[['a', 'c'], ['name', 'qualify']])  # list of labels and list of columns
print(data_dict.loc['a':'c', 'name':'qualify'])  # slicing (:) - don't use a list when slicing

## More on df Indexing
sales_data = pd.DataFrame({
    "name": ["William", "Emma", "Sofia", "Markus", "Edward", "Thomas", "Ethan", "Olivia", "Arun", "Anika", "Paulo"]
    , "region": ["East", "North", "East", "South", "West", "West", "South", "West", "West", "East", "South"]
    , "sales": [50000, 52000, 90000, 34000, 42000, 72000, 49000, 55000, 67000, 65000, 67000]
    , "expenses": [42000, 43000, 50000, 44000, 38000, 39000, 42000, 60000, 39000, 44000, 45000]})
print(sales_data)

# Printing the index
print(sales_data.index)
#  using one of the existing columns of the DataFrame as a new index
sales_data.set_index('name', inplace=True)
print(sales_data.index)
print(sales_data.loc['Markus'])
print(sales_data.loc['Markus', 'region'])

# sorting the index
sales_data.sort_index(inplace=True)  # (ascending=False)
print(sales_data)

sales_data.reset_index(inplace=True)
print(sales_data)
