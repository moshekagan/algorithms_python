import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# 1) sort by given list:
print('EX. 1')
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns = ["Col_A", "Col_B"])
print(df)
sort_list = ["C", "D", "B", "A"]
# solution:


# 2) insert a column at a specific location in DF
print('EX. 2')
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns = ["Col_A", "Col_B"])

print(df)
new_column = ["P", "Q", "R", "S"]
insert_position = 1

# solution:
df.insert(1,"col c",new_column)
print(df)

# 3) Select columns based on the column’s Data Type
print('EX. 3')
df = pd.DataFrame([["A", 1, True], ["B", 2, False],
                   ["C", 3, False], ["D", 4, True]],
                  columns=["col_A", "col_B", "col_C"])

print(df)
dt_type = "bool"

# solution:
df = df.loc[:,["col_C"]]
print(df)
# 4)  Count the number of Non-NaN cells for each column
print('EX. 4')
df = pd.DataFrame([["A", np.NaN], [np.NaN, 2],
                   ["C", np.NaN], ["D", 4]],
                  columns=["col_A", "col_B"])
print(df)
# solution
flt = df.shape[0]-df.isna().sum()
print(flt)
# 5)  Split DataFrame into equal parts
print('EX. 5')
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns=["col_A", "col_B"])
print(df)
parts = 2

# solution

# 6)  Reverse DataFrame row-wise or column-wise
print('EX. 6')
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns=["col_A", "col_B"])

print(df)

# solution

# 7)  Rearrange columns of a DataFrame
print('EX. 7')
df = pd.DataFrame([["A", 1], ["B", 2],
                   ["C", 3], ["D", 4]],
                  columns=["col_A", "col_B"])

rearrange_order = [1,0] # Column 1 then Column 0

print(df)

# solution

# 8)   Get alternate rows of a DataFrame
print('EX. 8')
df = pd.DataFrame([["A", 1], ["B", 2],
                   ["C", 3], ["D", 4]],
                  columns=["col_A", "col_B"])

print(df)

# solution

# 9)   Insert a row at an arbitrary position
print('EX. 9')
df = pd.DataFrame([["A", 1], ["B", 2], ["C", 3], ["D", 4]],
                  columns=["col_A", "col_B"])

insert_pos = 1
insert_row = ["P", 5]

print(df)

# solution

# 10)   Apply function to every cell of DataFrame
print('EX. 10')
df = pd.DataFrame([[1, 5], [2, 6], [3, 7], [4, 8]],
                  columns=["col_A", "col_B"])

def func(num):
    return num + 1

print(df)

# solution


# #EX. 1
#   Col_A  Col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#   Col_A  Col_B
# 2     C      3
# 3     D      4
# 1     B      2
# 0     A      1
# EX. 2
#   Col_A  Col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#   Col_A col_C  Col_B
# 0     A     P      1
# 1     B     Q      2
# 2     C     R      3
# 3     D     S      4
# EX. 3
#   col_A  col_B  col_C
# 0     A      1   True
# 1     B      2  False
# 2     C      3  False
# 3     D      4   True
#    col_C
# 0   True
# 1  False
# 2  False
# 3   True
# EX. 4
# col_A    3
# col_B    2
# dtype: int64
# EX. 5
#   col_A  col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#   col_A  col_B
# 0     A      1
# 1     B      2
#   col_A  col_B
# 2     C      3
# 3     D      4
# EX. 6
#   col_A  col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#    col_B col_A
# 0      1     A
# 1      2     B
# 2      3     C
# 3      4     D
#   col_A  col_B
# 3     D      4
# 2     C      3
# 1     B      2
# 0     A      1
# EX. 7
#   col_A  col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#    col_B col_A
# 0      1     A
# 1      2     B
# 2      3     C
# 3      4     D
# EX. 8
#   col_A  col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#   col_A  col_B
# 0     A      1
# 2     C      3
# EX. 9
#   col_A  col_B
# 0     A      1
# 1     B      2
# 2     C      3
# 3     D      4
#     col_A  col_B
# 0.0     A      1
# 1.0     B      2
# 2.0     C      3
# 3.0     D      4
# 0.9     P      5
#     col_A  col_B
# 0.0     A      1
# 0.9     P      5
# 1.0     B      2
# 2.0     C      3
# 3.0     D      4
#   col_A  col_B
# 0     A      1
# 1     P      5
# 2     B      2
# 3     C      3
# 4     D      4
# EX. 10
#    col_A  col_B
# 0      1      5
# 1      2      6
# 2      3      7
# 3      4      8
#    col_A  col_B
# 0      2      6
# 1      3      7
# 2      4      8
# 3      5      9