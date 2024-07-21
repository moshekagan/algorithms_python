import pandas as pd


def selection_sort(df, column_name):
    """
  Sorts a pandas DataFrame by a specific column using selection sort.

  Args:
      df: The pandas DataFrame to sort.
      column_name: The name of the column to sort by.

  Returns:
      A new pandas DataFrame with sorted rows.
  """
    # Make a copy to avoid modifying the original DataFrame
    df_sorted = df.copy()

    for i in range(len(df_sorted)):
        min_index = i
        for j in range(i + 1, len(df_sorted)):
            # pd.isna(df_sorted.loc[j, column_name]) or Handle potential missing values during comparison (replace with appropriate logic for your data)
            if df_sorted.loc[j, column_name] < df_sorted.loc[min_index, column_name]:
                min_index = j

        # Swap rows (ensure correct handling of missing values if needed)
        if min_index != i:
            df_sorted.iloc[[i, min_index]] = df_sorted.iloc[[min_index, i]]

    return df_sorted


if __name__ == '__main__':
    # Sample data (replace with your actual data)
    data = {'col1': [5, 2, 8, 1, 4], 'col2': ['c', 'a', 'b', 'd', 'e']}
    df = pd.DataFrame(data)
    print(df)
    # Sort by 'col1' in ascending order (modify for descending order)
    sorted_df = selection_sort(df.copy(), 'col1')

    # Print the sorted DataFrame
    print(sorted_df)
