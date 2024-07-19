import pandas as pd
import numpy as np

class Data_Analyzer():
    def __init__(self,fname):
        self.df = pd.read_csv(fname)
    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def percent_nans(self):
        #  Area - 0%
        #  Year - 0%
        #  import - 0%
        #  export - 40%

        # Option A
        # count all rows
        column_percent_nans = {}
        count_all_row = self.df.shape[0]
        columns = self.df.columns
        for c in columns:
            # count rows in column with Nan
            current_column = self.df[c]
            nans = current_column.isna()
            count_nans = nans.sum()

            # calc_percent = (rows with Nan) / (all row) * 100
            calc_percent = (count_nans / count_all_row) * 100

            # save calc_percent for column 'c'
            column_percent_nans[c] = calc_percent

        res = pd.Series(column_percent_nans)
        return res

        # Option B
        # return self.df.isna().mean() * 100

        # # Option C
        # rows = self.df.shape[0]
        #
        # area_nan = self.df["Area"].isna()
        # area_nan_sum = area_nan.sum()
        # year_nan = self.df["Year"].isna()
        # year_nan_sum = year_nan.sum()
        # import_nan = self.df["import"].isna()
        # import_nan_sum = import_nan.sum()
        # export_nan = self.df["export"].isna()
        # export_nan_sum = export_nan.sum()
        #
        # area_nan_percent = (area_nan_sum / rows) * 100
        # year_nan_percent = (year_nan_sum / rows) * 100
        # import_nan_percent = (import_nan_sum / rows) * 100
        # export_nan_percent = (export_nan_sum / rows) * 100
        #
        # return pd.Series([area_nan_percent, year_nan_percent, import_nan_percent, export_nan_percent], index=["Area", "Year", "import", "export"])

    # Q2
    def replace_nans(self):
        self.df = self.df.fillna(0)
        # OR
        # self.df.fillna(0, inplace=True)
        return True

    # Q3
    def omit_zero_lines(self,colnames=["import", "export"]):
        filter = self.df[colnames] == 0
        # filter_2 = ~filter.all(axis=1)
        filter_2 = filter.all(axis=1) == False
        self.df = self.df[filter_2]
        self.df = self.df.reset_index()

    # Q4
    def calc_diff(self,col1,col2,newcol):
        def f(df, col1, col2):
            return pd.Series(df[col1] - df[col2])

        # self.df.apply(f, args=[col1, col2])
        newcol_values = self.df.apply(f, col1=col1, col2=col2, axis=1)
        self.df[newcol] = newcol_values

    # Q5
    def flt(self,group_col = "Area",val = "", threshold = 0):
        pass


    # Q6
    def merge(self,left, right,col = "netVal"):
        pass
    def merge_sort(self,L,col = "netVal"):
      pass

    # Q7
    def binary_search(self,d, low, high, x, col="netVal"):
        pass

def main():
    data = Data_Analyzer('import_export.csv')
    print(data)

    # Q1
    print(data.percent_nans())
    # Q2
    data.replace_nans()
    print(data.percent_nans())

    # Q3
    data.omit_zero_lines(colnames = ["import", "export"])

    # Q4
    data.calc_diff("export", "import", "netVal")
    print(data.df.head())

    # Q5
    arr = data.flt(group_col = "Area",val="netVal", threshold=0)
    arr = arr[["Year","netVal"]].sort_values(by="netVal").reset_index(drop=True)
    arr.to_csv("sorted_netVal.csv",index=False)
    arr = pd.read_csv("sorted_netVal.csv")

    # Q6
    i = data.binary_search(arr,0,arr.shape[0]-1,np.round(arr["netVal"].mean()),"netVal")
    print(np.round(arr["netVal"].mean()))
    print(arr.iloc[i-1:i+1])


    i = data.binary_search(arr, 0, arr.shape[0] - 1, np.round(arr["netVal"].max()), "netVal")
    print(np.round(arr["netVal"].max()))
    print(arr.iloc[i])

    i = data.binary_search(arr, 0, arr.shape[0] - 1, np.round(arr["netVal"].min()), "netVal")
    print(np.round(arr["netVal"].min()))
    print(arr.iloc[i])

if __name__=="__main__":
    main()
