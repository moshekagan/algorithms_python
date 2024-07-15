import pandas as pd
import numpy as np

letters = [chr(i) for i in range(97,123)]
a=np.random.normal(loc=0.5, scale = 1, size=len(letters))
s = pd.Series(a,index=letters,dtype = 'float')
print(s.values)
print(s.index)
print(s.dtype)

d = {'a':1,'b':10,'c':100}
s_d = pd.Series(d,dtype = 'int32')
# slicing Series as list
# index slicing [from:to(not including):step]
print(s[2:10:2])
print(s[:-3])
print(s[::-1])

# slicing Series as dictionary
print(s['d'])
print(s['d':'k'])
a = s['d':'k']
print(s['d':'k':3])
print(f"is 'k' in s? {'k' in s}")
# s['zz'] # KeyError
s.get("zz",-1) # surpasses KeyErrors, like dictionary method
# can operate on pandas series with math functions
print(s.mean(),s.std(),s.sem())
# can treat series like a vector
print(s*s)
print(5*s)

# can treat a Serie as time Serie and operate on it
m = abs(s)>abs(s).mean() # boolean series, same keys and dimension as s
print(s[m]) # filter series using mask m
print(s[(s>-0.5) & (s<0.5)])
print(s.index[(s>-0.5) & (s<0.5)])
print(s.values[(s>-0.5) & (s<0.5)])
print(s[(s<-0.5) | (s>0.5)])

df = pd.DataFrame()
print(df)
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, 9, 9, 20, 14.5, 7, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
data_exam = pd.DataFrame(exam_data)
# data_exam.index = data_exam["name"]
# data_exam = data_exam.loc[:,"score":]

data = [['tom', 10], ['nick', 15], ['juli', 14]]
df = pd.DataFrame(data, columns=['Name', 'Age'])

data_csv = pd.read_csv('diamonds.csv')
data_csv.describe() # summarizing table
print(data_csv.head(10))
print(data_csv.tail(10))
print(data_csv.info())
print(data_csv.shape)
print(data_csv.columns)
print(data_csv.index)

# column slicing
# Getting one column
print(data_csv['cut'])
print(type(data_csv['cut']))
print(data_csv['cut'].value_counts()) # number of appearances per category in categorial variable
print(data_csv['cut'].unique())  # column's unique values
print(set(data_csv['cut']))  # column's unique values
print(data_csv['cut'].nunique())


