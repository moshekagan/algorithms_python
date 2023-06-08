import pandas as pd
import numpy as np


class Data_Preprocess():
    def __init__(self, fname):
        self.df = pd.read_pickle(fname)
        random_rows = self.df.sample(n=10000)
        random_rows.to_csv('random_rows_data_pickles.csv', index=False)

        # self.df = pd.read_csv('random_rows_data_pickles.csv')

    def intro(self):
        # print(self.df)
        print(self.df.columns)
        print(self.df.info())
        # print(self.df.describe())

    def describe_object(self, colname):
        print("----------describe_object-------------")
        column_count = self.df[colname].value_counts()
        print(column_count)

        return column_count

    def describe_all(self, column_index):
        if not 0 <= column_index < self.df.shape[1]:
            return

        column = self.df.iloc[:, column_index]
        is_numeric = np.issubdtype(column.dtype, np.number)

        if is_numeric:
            print("----------is_numeric-------------")
            print(column.describe())
        else:
            self.describe_object(column.name)

        self.describe_all(column_index + 1)

    def _update_index(self):
        self.df.index = list(range(self.df.shape[0]))

    def omit_zeros(self):
        self.df = self.df[self.df['Value'] != 0]
        self._update_index()

    def filt_top_areas_by_unit(self, unit, number):
        mask = self.df['Unit'] == unit
        u_df = self.df[mask]
        print(u_df.shape)

        area_count = self.describe_object("Area")
        top_areas = area_count.nlargest(number).index
        self.df = u_df[u_df["Area"].isin(top_areas)]
        self._update_index()

    def drop_cols(self, columns):
        self.df = self.df.drop(columns=columns)

    def calc_stats_by_factors(self, df, factors, vals, funcs):
        grouped_data = df.groupby(factors)
        grouped_data = grouped_data[vals]
        grouped_data = grouped_data.agg(funcs)

        return grouped_data

    def norm_by_factors(self, cols):
        # Calculate mean and standard deviation per category
        a = self.df.groupby(cols)['Value']
        grouped_stats_mean = a.transform('mean')
        grouped_stats_std = a.transform('std')

        # Calculate normalized values
        normed_val = (self.df['Value'] - grouped_stats_mean) / grouped_stats_std

        # Add normalized values as a new column
        self.df['normed_val'] = normed_val

    def split_by_factor(self, factor, val):
        df = self.df[self.df[factor] == val]
        df.index = list(range(df.shape[0]))

        return df

    def merge_dfs(self, s1, s2, colnames):
        # Create DataFrames from the input series
        df1 = pd.DataFrame(s1)
        df2 = pd.DataFrame(s2)

        # Merge the DataFrames based on the common index and colnames
        merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how='inner')
        merged_df.columns = colnames

        return merged_df

    def diff_cols(self, dat, col1, col2):
        return dat[col1] - dat[col2]

    def apply_diff_cols(self, d, c1, c2, newcol):
        n_col = d.apply(self.diff_cols, args=(c1, c2), axis=1)
        d[newcol] = n_col

        return d


def main():
    data = Data_Preprocess('data.pickle')
    # 1.
    data.intro()

    data.describe_object("Area")

    # 2. + 3.
    data.describe_all(0)

    # 4.
    data.omit_zeros()
    print("4. after omitting zeros df shape is ", data.df.shape)
    print(data.df.head())

    # 5.
    data.filt_top_areas_by_unit('tonnes', 5)
    print("5. After filtering product tonnes from 5 most reported areas, df shape is ", data.df.shape)
    print(data.df.head())

    # 6.
    data.drop_cols(["Item", "Unit"])
    print("df shape after cols reduction", data.df.shape)

    # 7.
    # group by year+element, calculate annual mean and std of export and import quantities
    print("annual mean and std of export and import quantities")
    print(data.calc_stats_by_factors(data.df, ["Year", "Element"], "Value", [np.mean, np.std]))
    print()

    # 8.
    # apply z-score normalization by Year
    data.norm_by_factors(["Year"])
    print("after z-score normalization by Year\n")
    print(data.df.head(10))
    print(data.df.shape)

    # 9.
    data.export_df = data.split_by_factor("Element", "Export Quantity")
    print("Export dataframe shape is ", data.export_df.shape)
    print("Export dataframe head:\n", data.export_df.head())
    data.import_df = data.split_by_factor("Element", "Import Quantity")
    print("Import dataframe shape is ", data.import_df.shape)
    print("Import dataframe head:\n", data.import_df.head())

    # Additional tests on export/import data
    data.export_df = data.calc_stats_by_factors(data.export_df, ["Area", "Year"], "Value", np.mean)
    print("export dataframe stats shape is ", data.export_df.shape)
    print(data.export_df.head())
    data.import_df = data.calc_stats_by_factors(data.import_df, ["Area", "Year"], "Value", np.mean)
    print("import dataframe stats shape is ", data.import_df.shape)
    print(data.import_df.head())

    # 10.
    data.merged = data.merge_dfs(data.import_df, data.export_df, ["Import", "Export"])
    print("merged Export-Import dataframe shape is ", data.merged.shape)
    print("merged Export-Import head:\n", data.merged.head())

    # 11.
    data.merged = data.apply_diff_cols(data.merged, c1="Export", c2="Import", newcol='GNI')
    print("merged Export-Import dataframe with GNI looks like this:")
    print(data.merged.head(10))


if __name__ == "__main__":
    main()
