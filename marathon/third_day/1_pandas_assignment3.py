import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame


class Data_Preprocess():
    def __init__(self, fname):
        self.df = pd.read_pickle(fname)
        # subset data:
        # random_rows = self.df.sample(n=10000)
        # random_rows.to_csv('random_rows_data_pickles.csv', index=False)

        # self.df = pd.read_csv('random_rows_data_pickles.csv')

    def intro(self):
        print(self.df.columns)
        print(self.df.shape)
        print(self.df.info())

    def describe_object(self, colname):
        col = self.df[colname]
        column_count = col.value_counts()
        print(column_count)

        return column_count

        # BAD:
        # res = {}
        # u = col.unique()
        # for i in u:
        #     mask = col.isin([i])
        #     r = len(col[mask])
        #     res[i] = r
        #
        # return res

    def describe_all(self, num):
        if 0 <= num < len(self.df.columns):
            # column_name = self.df.columns[num]

            # describe column num:
            column = self.df.iloc[:, num]

            is_numeric = np.issubsctype(column.dtype, np.number)

            # Bad:
            # if column.dtype in [np.int64, np.float64]:
            #     is_numeric = True
            # else:
            #     is_numeric = False

            if is_numeric == True:
                print(column.name)
                print(column.describe())
            else:
                self.describe_object(column.name)

            self.describe_all(num + 1)

    def omit_zeros(self):
        # remove 0 from "Value"
        mask = (self.df["Value"] != 0)
        df_non_zero_values = self.df[mask]
        df_non_zero_values = df_non_zero_values.dropna()
        df_non_zero_values = df_non_zero_values.reset_index()
        # Other option:
        # df_non_zero_values.index = list(range(len(df_non_zero_values)))

        self.df = df_non_zero_values
        return True

    def filt_top_areas_by_unit(self, u, n):
        mask = self.df["Unit"] == u
        f_df = self.df[mask]

        area_count = f_df["Area"].value_counts()
        top_n = area_count.nlargest(n)

        top_n_areas = top_n.index
        mask_2 = f_df["Area"].isin(top_n_areas)
        f_df = f_df[mask_2]

        self.df = f_df

    def drop_cols(self, columns_names):
        self.df = self.df.drop(columns=columns_names)

    def calc_stats_by_factors(self, df, factors, vals, funcs):
        grouped_df = df.groupby(factors)
        val_grouped_df = grouped_df[vals]
        agg_val_grouped_df = val_grouped_df.agg("mean")

        # Year Element Value
        # 1961 Export   5
        # 1961 Export   3
        # 1961 Export   4

        # => agg("mean)
        # 1961 Export   4 (mean)

        # => transform("mean)
        # Year Element mean
        # 1961 Export   4
        # 1961 Export   4
        # 1961 Export   4

        return agg_val_grouped_df

    def norm_by_factors(self):
        pass

    def split_by_factor(self):
        pass

    def merge_dfs(self):
        pass

    def diff_cols(self, dat, col1, col2):
        return dat[col1] - dat[col2]

    def apply_diff_cols(self, d, c1, c2, new_col_name):
        # newcol = self.diff_cols(d, c1, c2)
        newcol = d.apply(func=self.diff_cols, args=[c1, c2], axis=1)
        d[new_col_name] = newcol

        return d


def main():
    data = Data_Preprocess('/Users/moshekagan/repos/algorithms_python/Assigments/3/data.pickle')
    # 1.
    data.intro()

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

    # 8.
    # apply z-score normalization by Year
    # data.norm_by_factors(["Year"])
    # print("after z-score normalization by Year\n")
    # print(data.df.head(10))
    # print(data.df.shape)

    # 9.
    # data.export_df = data.split_by_factor("Element","Export Quantity")
    # print("Export dataframe shape is ",data.export_df.shape)
    # print("Export dataframe head:\n", data.export_df.head())
    # data.import_df = data.split_by_factor("Element", "Import Quantity")
    # print("Import dataframe shape is ",data.import_df.shape)
    # print("Import dataframe head:\n", data.import_df.head())

    # Additional tests on export/import data
    # data.export_df = data.calc_stats_by_factors(data.export_df,["Area","Year"],"Value",np.mean)
    # print("export dataframe stats shape is ",data.export_df.shape)
    # print(data.export_df.head())
    # data.import_df = data.calc_stats_by_factors(data.import_df,["Area","Year"],"Value",np.mean)
    # print("import dataframe stats shape is ",data.import_df.shape)
    # print(data.import_df.head())

    # 10.
    # data.merged = data.merge_dfs(data.import_df,data.export_df,["Import","Export"])
    # print("merged Export-Import dataframe shape is ",data.merged.shape)
    # print("merged Export-Import head:\n",data.merged.head())

    # 11.
    # data.merged = data.apply_diff_cols(data.merged,c1="Export",c2="Import",newcol='GNI')
    # print("merged Export-Import dataframe with GNI looks like this:")
    # print(data.merged.head(10))


if __name__ == "__main__":
    main()
