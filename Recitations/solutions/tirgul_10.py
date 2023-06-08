import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('titanic.csv')
print(df)

pd.set_option("display.max_columns", 10)
print(df)

new_columns_names = {'Survived': 'SURVIVED','Pclass': 'PCLASS' ,
                     'Name': "NAME", 'Sex': 'SEX', 'Age': 'AGE',
                     'Siblings/Spouses Aboard': 'SIBSA',
                     "Parents/Children Aboard": 'PARCA', 'Fare': "FARE"}

df.rename(columns = new_columns_names, inplace = True)
print(df)

#df = df.rename(columns = new_columns_names)


select_cols = ['SURVIVED', 'PCLASS', 'AGE', 'FARE']
df2 = df[select_cols]
print(df2)

#6
print(df.isnull().any())
print(df.isnull().any(axis=1))
#
# for i in df.iterrows():
#     print(i)

for i, row in df.iterrows():
    print("index:", i)
    print(row)
    if (i+1)%3 ==0:
        x = input("enter q to stop")
        if x == 'q':
            break

print(df.groupby('PCLASS').mean())
print(df.groupby('PCLASS').sum().reset_index())


tmp_df = df2.groupby('PCLASS').mean()
tmp_df['SURVIVED'] = tmp_df['SURVIVED'] * 100
print(tmp_df)
tmp_df.plot(kind = 'bar')
plt.show()

'from the mudele'
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# data downloaded from here: https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html
df = pd.read_csv('titanic.csv')

print(df)

print(df.columns)
pd.set_option("display.max_columns", 10)

new_columns_names = {'Survived': 'SURVIVED','Pclass': 'PCLASS'
                        ,'Name': "NAME", 'Sex': 'SEX', 'Age': 'AGE',
                     'Siblings/Spouses Aboard': 'SIBSA',
                     "Parents/Children Aboard": 'PARCA', 'Fare': "FARE"}

df.rename(columns=new_columns_names, inplace=True)

# 2nd way:
# df = df.rename(columns=new_columns_names, inplace=False)
select_cols = ['SURVIVED', 'PCLASS', 'AGE', 'FARE']

df_with_selected_cols = df[select_cols]
print(df_with_selected_cols)

print(df.describe())

print(df.isnull().any())
print(df.isnull().any(axis=1))


for i, row in df.iterrows():
    print("index:", i)
    print(row)
    if (i+1) % 3 == 0:
        x = input("press q to stop or any other key to continue")
        if x == 'q':
            break

print(df_with_selected_cols.groupby('PCLASS').mean())

print(df_with_selected_cols.groupby('PCLASS').sum().reset_index())

tmp_df = df_with_selected_cols.groupby('PCLASS').mean()
tmp_df.loc[:,'SURVIVED'] *=100
print(tmp_df)
tmp_df.plot(kind='bar')

plt.show()
