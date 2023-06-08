import pandas as pd

# Filtering data
data_csv = pd.read_csv('diamonds.csv')
print(data_csv.head())

# Find all the rows with cut=Ideal
flt = data_csv['cut'] == 'Ideal'
ideal_cut = data_csv[flt]
print(data_csv[flt])

# Find all the rows with cut=Ideal and color=E
flt = (data_csv['cut'] == 'Ideal') & (data_csv['color'] == 'E')
ideal_cut_color = data_csv[flt]
print(ideal_cut_color.head())
print(ideal_cut_color.shape)

# Filtering using loc
print(data_csv.loc[flt, ['carat', 'price']])
print()

# Filtering using query method
print(data_csv.query("cut=='Ideal'& color=='E'"))

# Filtering using isin method
cuts = ['Ideal', 'Premium']
mask = data_csv['cut'].isin(cuts)
print(data_csv[mask])
print()

# Filtering using str method
# str methods

mask = data_csv['cut'].str.contains('V')
print(data_csv[mask])
print()

# Manipulating data

sales_data = pd.DataFrame({
    "name": ["William", "Emma", "Sofia", "Markus", "Edward", "Thomas", "Ethan", "Olivia", "Arun", "Anika", "Paulo"]
    , "region": ["East", "North", "East", "South", "West", "West", "South", "West", "West", "East", "South"]
    , "sales": [50000, 52000, 90000, 34000, 42000, 72000, 49000, 55000, 67000, 65000, 67000]
    , "expenses": [42000, 43000, 50000, 44000, 38000, 39000, 42000, 60000, 39000, 44000, 45000]})
print(sales_data)

print(sales_data.columns)
print()
sales_data.rename(columns={'name': 'firstname'}, inplace=True)
print(sales_data.columns)
print()

sales_data.columns = [x.capitalize() for x in sales_data.columns]
print(sales_data.columns)
print()

# Adding a new column

# using a list
discount = [10, 20, 12, 32, 10, 15, 25, 15, 10, 20, 5]
sales_data['Discount'] = discount
print(sales_data)

# using another column (or columns) of the dataframe
sales_data['Benefit'] = sales_data['Sales'] - sales_data['Expenses']
print(sales_data)

# Removing a column
sales_data.drop('Discount', axis=1, inplace=True)  # axis=1 for ropping a column
print(sales_data)

# Updating rows values
sales_data.loc[2, ['Sales', 'Expenses']] = [55000, 10000]
print(sales_data)
print()

sales_data.loc[2] = ['Anna', 'East', 15000, 10000, 50000]  # updating the third row
print(sales_data)
print()

# Updating Rows and Columns Based On Condition
filt = (sales_data['Sales'] > 65000)
sales_data.loc[filt, 'Benefit'] = sales_data['Benefit'] * 1.5
# sales_data[filt]['Benefit'] = sales_data['Benefit']*1.5     -----   is not the correct syntax
print(sales_data)
print()

# Updating using apply method
# Example 1 - applying len() function

sales_data['Namelen'] = sales_data['Firstname'].apply(len)
print(sales_data)
print()


# Example 2 - applying custom function

def rate(x):
    if x > 55000:
        return 'good'
    else:
        return "bad"


sales_data['Rate'] = sales_data['Sales'].apply(rate)
print(sales_data)
print(sales_data.head())


def rate2(x, y):
    return x - y > 0


sales_data['yield'] = sales_data.apply(lambda x: rate2(x['Sales'], x['Expenses']), axis=1)
print(sales_data.head())
# equivalent to
sales_data['yield'] = sales_data['Sales'] - sales_data['Expenses']
print(sales_data.head())
