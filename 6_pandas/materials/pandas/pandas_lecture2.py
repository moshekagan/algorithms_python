import pandas as pd

# Filtering data
data_csv=pd.read_csv('diamonds.csv')
print(data_csv.head())

# Find all the rows with cut=Ideal
flt=data_csv['cut']=='Ideal'
print(data_csv[flt].head())

# Find all the rows with cut=Ideal and color=E
flt= (data_csv['cut']=='Ideal') & (data_csv['color']=='E')
print(data_csv[flt].head())

#Filtering using loc
print(data_csv.loc[flt,['carat','price']].head())

# Filtering using query method
print(data_csv.query("cut=='Ideal'& color=='E'").head())

# Filtering using isin method
cuts=['Ideal','Premium']
mask=data_csv['cut'].isin(cuts)
print(data_csv.loc[mask].shape)

# Filtering using str method
#str methods
mask=data_csv['cut'].str.contains('V')
print(data_csv[mask].head())

# Data Manipulations
sales_data = pd.DataFrame({
"name":["William","Emma","Sofia","Markus","Edward","Thomas","Ethan","Olivia","Arun","Anika","Paulo"]
,"region":["East","North","East","South","West","West","South","West","West","East","South"]
,"sales":[50000,52000,90000,34000,42000,72000,49000,55000,67000,65000,67000]
,"expenses":[42000,43000,50000,44000,38000,39000,42000,60000,39000,44000,45000]})
print(sales_data)
print(sales_data.columns)

# renaming column names
sales_data.rename(columns={'name': 'firstname'}, inplace=True)
print(sales_data.columns)

sales_data.columns=[x.capitalize() for x in sales_data.columns]
print(sales_data.columns)

# Adding a new column
# using a list
discount=[10,20,12,32,10,15,25,15,10,20,5]
sales_data['Discount']=discount
print(sales_data)

# using derived data from another column (or columns) in the dataframe
sales_data['Benefit']=sales_data['Sales']-sales_data['Expenses']
print(sales_data)

# Removing a column
sales_data.drop('Discount', axis=1,inplace=True)    # axis=1 for column removal
print(sales_data)

# Updating rows values - dimensions must match
sales_data.loc[2,['Sales','Expenses']]= [55000,10000]
print(sales_data)

# row assignment
sales_data.loc[2]=['Anna','East',15000,10000,50000]
print(sales_data)

# Updating filtered row/column entries using 'loc' mask slicing
filt = (sales_data['Sales'] > 65000)
sales_data.loc[filt,'Benefit'] = sales_data['Benefit']*1.5
print(sales_data)

# Updating using apply method
# Example 1 - applying len() function
sales_data['Namelen']=sales_data['Firstname'].apply(len)
print(sales_data.head())

# Example 2 - applying custom function
def rate(x):
    if x> 55000:
        return 'good'
    else:
        return "bad"

sales_data['Rate']=sales_data['Sales'].apply(rate)
print(sales_data)

def rate2(df):
    return df['Sales']-df['Expenses']>0
# Example 3 - applying lambda function
sales_data['Profit']=sales_data.apply(rate2,axis=1)
sales_data['Profit']=sales_data.apply(lambda df: df['sales']-df['expenses']>0 ,axis=1)
# similar to:
sales_data['Profit'] = sales_data['Sales']-sales_data['Expenses']>0