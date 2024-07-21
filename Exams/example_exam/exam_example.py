# ===============  Question 1   =======================
import pandas as pd

# Load data (replace with your actual file path)
data = pd.read_csv("library_loans.csv", header=0)

# Drop rows with any NaN value
data = data.dropna()

# Get list of columns with numerical data types (excluding strings)
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

print(numerical_cols)
data[numerical_cols] = data[numerical_cols].abs()



def is_valid_month(month_name):
    """
  Checks if a string is a valid month name (January to December).

  Args:
      month_name: The string to be checked.

  Returns:
      True if the string is a valid month name, False otherwise.
  """
    # Define a set of valid month names (all lowercase for case-insensitive matching)
    valid_months = {'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
                    'nov', 'dec'}
    return month_name.lower() in valid_months  # Title case for case-insensitive check


# Create a function to check validity and drop rows with invalid names
def clean_month_data(df):
    df['is_valid_month'] = df['month'].apply(is_valid_month)
    print(df.head(10))
    return df.query('is_valid_month == True')  # Filter rows with True in 'is_valid_month'


# Clean the DataFrame
data = clean_month_data(data.copy())  # Avoid modifying original DataFrame
print(data.head())
data = data.drop('is_valid_month', axis=1)
print(data.head())


# Group data by genre and month
grouped_data = data.groupby(["genre", "month"])
print(grouped_data)
results = grouped_data.agg(
    avg_loan_duration=("loan_duration", "mean"),
    renewal_rate=("is_renewal", lambda x: (x == True).mean()),
    min_book_id=("book_id", lambda x: x.min())
)
print(results)

# most popular genre
target = int(input("Please enter number of most popular genres: "))

genre_counts = data['genre'].value_counts()
print(genre_counts)
# Print results in a formatted table
print(genre_counts[:target])


from modified_selection_sort import min_max_selection_sort
print(min_max_selection_sort(data['genre'].tolist()))


from pandas_selectionsort import selection_sort
data = data.reset_index(drop=True)
print(selection_sort(data.copy(), 'genre'))



# ===============  Question 2   =======================#
#      How can you improve the best case efficiency    #
#      in bubble sort? (The input is already sorted)   #
# =====================================================#

def improved_bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            print("No swaps in this iteration, array is sorted")
            break

    return arr


# Example usage with already sorted array
arr = [1, 2, 3, 4, 5]
sorted_arr = improved_bubble_sort(arr.copy())  # Avoid modifying original array

print(sorted_arr)  # Output: [1, 2, 3, 4, 5] (No swaps, early termination)

