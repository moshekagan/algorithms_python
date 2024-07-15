import pandas as pd
import numpy as np
letters = [chr(i) for i in range(97,123)]
a=np.random.normal(loc=0.5, scale = 1, size=len(letters))
s = pd.Series(a,index=letters,dtype = 'float16')
print(s.values)
print(s.index)
print(s.dtype)

d = {'a':1,'b':10,'c':100}
s_d = pd.Series(d,dtype = 'int32')

# index slicing [from:to(not including):step]
print(s[2:10:2])
print(s[:-3])
print(s[::-1])
print(s[10])

# dictionary like processing
print(s['d'])
print(s['d':'k']) # including the last one
print(s['d':'k':3])
print(f"is 'k' in s? {'k' in s}")
print(s['zz'])
print(s.get('zz',-1))

# use numerical methods on series
print(s.mean(),s.std(),s.sem())
print(3*s)
print(s*s)

mask = abs(s)<abs(s).mean()
print(s[mask])
s[mask].index
# complex condition statement filtering
mask2 = (s>s.mean()-0.5*s.std()) & (s<s.mean()+0.5*s.std())
print(s[mask2])

mask2 = (s<s.mean()-0.5*s.std()) | (s>s.mean()+0.5*s.std())
print(s[mask2])

# pandas DataFrame - 2D hashtable
df = pd.DataFrame()
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, 9, 9, 20, 14.5, 7, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
data_exam = pd.DataFrame(exam_data)
print(type(data_exam))



