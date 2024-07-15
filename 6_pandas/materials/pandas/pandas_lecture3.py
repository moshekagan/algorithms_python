import pandas as pd
import numpy as np

employees=pd.read_csv('employees.csv')
print(employees.info())
print(np.round(employees.describe(),2))
print(employees.shape)

# To check missing values in Pandas DataFrame,
# we use a function isna() (or isnull() ) and notna() (or notnull() ).
flt=employees['Gender'].isna()
flt2 = employees["Gender"].isnull()
print(employees.loc[flt,['First Name','Gender','Salary']])

# Filling missing values using fillna() or replace()
# using fillna()
emp=employees["Gender"].fillna("No Gender")
print(emp)
#using replace() and inplace=True
employees.replace(np.NaN,'No Gender',inplace=True)
print(employees.head())
# fillNa by column rule:
fillna_rule = {"Gender":'No Gender',
              'First Name':"No Name",
              'Senior Management':'No Management'}
print(employees.fillna(value=fillna_rule,inplace=True))

# Dropping missing values using dropna()
# df.dropna(how=‘any’) drop rows with at least one Nan value
# df.dropna(how=‘all’) drop rows where all values are Nans
# df.fillna(value=3) replace Nans with another value
# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95, np.nan],
        'Second Score': [30, np.nan, 45, 56, np.nan],
        'Third Score': [52, 40, 80, 98, np.nan],
        'Fourth Score': [np.nan, np.nan, np.nan, 65, np.nan]}
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
df1=df.dropna()
print(df1)

# drop a rows whose all data is missing or contain null values(NaN)
df1=df.dropna(how = 'all')
print(df1)
#drop a rows with at least 1 null value
df1=df.dropna(axis = 0, how ='any')
print(df1)

#Dropping columns with at least 1 null value
df1=df.dropna(axis = 1)
print(df1)

#    Sorting
exam  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, 9, 9, 20, 14.5, 7, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

data_exam=pd.DataFrame(exam)
print(data_exam)
data1=data_exam.sort_values('name')
print(data1)

# or using inplace=True if we want to make the change in the same DataFrame
data_exam.sort_values('name',inplace=True)
print(data_exam)

# more examples
print(data_exam.sort_values(['score','attempts'],ascending=[True,False]))

print(data_exam.sort_values(['score','attempts'],ascending=[1,0]))

print(data_exam.sort_values(['score','attempts'],ascending=[1,0],inplace=True))

print(data_exam.nsmallest(3,'score'))

print(data_exam.nlargest(3,'score'))

# Vectorized mathematical operations:
# generate DatetimeIndex index
dates = pd.date_range(start = '26/02/2023', end = '09/06/2023', periods=13)
df = pd.DataFrame(np.random.randn(13,4), index=dates, columns=list('ABCD'))
# calculate mean by column
df.mean()
# mean by row
df.mean(axis = 1)
s = pd.Series(range(1,len(dates)+1), index = dates)
df.sub(s, axis='index')

# Dataframes concatenation
# pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, copy=True)
# create 3 letter dataframes with equal column length:
df1 = pd.DataFrame(np.random.randint(97,123,size = [4,4]),columns=['a','b','c','d'])
df1 = df1.apply(lambda x: pd.Series([chr(i) for i in x],index=df1.columns),axis=1)
df2 = pd.DataFrame(np.random.randint(97,123,size = [4,4]),columns=['a','b','c','d'])
df2 = df2.apply(lambda x: pd.Series([chr(i) for i in x],index=df1.columns),axis=1)
df3 = pd.DataFrame(np.random.randint(97,123,size = [4,4]),columns=['a','b','c','d'])
df3 = df3.apply(lambda x: pd.Series([chr(i) for i in x],index=df1.columns),axis=1)
df_merged_0 = pd.concat([df1,df2,df3],axis=0)
df_merged_1 = pd.concat([df1,df2,df3],axis=1)
df3 = df3.iloc[1:,1:]
# merging with unequal sizes:
# inclusive merging - join = 'outer', fills with Nans missing entries
df_merged_2 = pd.concat([df1,df3],axis=1,join = 'outer')
# reductive merging - join = 'inner', cuts out missing keys
df_merged_3 = pd.concat([df1,df3],axis=0,join = 'inner')

# df.append appends rows (only) to existing dataframe
# ignore_index resets index
df_append = df1.append(df2,ignore_index=False)

