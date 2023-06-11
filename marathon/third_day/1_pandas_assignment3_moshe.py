import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame


class Data_Preprocess():
    def __init__(self, fname):
        # self.df = pd.read_pickle(fname)
        # random_rows = self.df.sample(n=10000)
        # random_rows.to_csv('random_rows_data_pickles.csv', index=False)

        self.df = pd.read_csv('random_rows_data_pickles.csv')

    def intro(self):
        print(self.df.columns)
        print(self.df.shape)
        print(self.df.info())

    def describe_object(self, colname):
        print(self.df[colname].value_counts())

    def describe_all(self, num):
        if num >= len(self.df.columns):
            return

        col_name = self.df.columns[num]
        col = self.df[col_name]

        if np.issubsctype(col.dtype, np.number):
            print(col.describe())
        else:
            self.describe_object(col_name)

        self.describe_all(num+1)

    def omit_zeros(self):
        pass

    def filt_top_areas_by_unit(self):
        pass

    def drop_cols(self):
        pass

    def calc_stats_by_factors(self):
        pass

    def norm_by_factors(self):
        pass

    def split_by_factor(self):
        pass

    def merge_dfs(self):
        pass

    def diff_cols(self):
        pass

    def apply_diff_cols(self):
        pass


def main():
    data = Data_Preprocess('/Users/moshekagan/repos/algorithms_python/Assigments/3/data.pickle')
    # 1.
    data.intro()

    # 2. + 3.
    data.describe_all(0)

    # 4.
    # data.omit_zeros()
    # print("4. after omitting zeros df shape is ", data.df.shape)
    # print(data.df.head())

    # 5.
    # data.filt_top_areas_by_unit('tonnes',5)
    # print("5. After filtering product tonnes from 5 most reported areas, df shape is ", data.df.shape)
    # print(data.df.head())

    # 6.
    # data.drop_cols(["Item","Unit"])
    # print("df shape after cols reduction",data.df.shape)

    # 7.
    # group by year+element, calculate annual mean and std of export and import quantities
    # print("annual mean and std of export and import quantities")
    # print(data.calc_stats_by_factors(data.df,["Year","Element"],"Value",[np.mean,np.std]))

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
