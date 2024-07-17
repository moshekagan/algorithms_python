import pandas as pd
import numpy as np

class Data_Analyzer():
    def __init__(self,fname):
        self.df = pd.read_csv(fname)
    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def percent_nans(self):
        rows = self.df.shape[0]

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

        column_nan_percent = {}
        for c in self.df.columns:
            nans = self.df[c].isna()
            nan_sum = nans.sum()
            column_nan_percent[c] = (nan_sum / rows) * 100

        return pd.Series(column_nan_percent)

    # Q2
    def replace_nans(self):
        self.df = self.df.fillna(0)

    # Q3
    def omit_zero_lines(self,colnames=["import","export"]):
        filter = self.df[colnames] == 0
        self.df = self.df[~filter.all(axis=1)]
        a = self.df.reset_index(drop=False)
        self.df = self.df.reset_index(drop=True)


    # Q4
    def calc_diff(self, col1, col2, newcol):
        # option 1
        a = self.df[col1] - self.df[col2]
        self.df[newcol] = a

        def f(data, col1, col2):
            return data[col1] - data[col2]
        # print(f(self.df, col1, col2))
        self.df[newcol] = self.df.apply(f, col1=col1, col2=col2, axis=1)
        # print(self.df)

    # Q5
    def flt(self,group_col = "Area",val = "", threshold = 0):
        # Option A
        # groups = self.df.groupby(group_col)
        # print(groups)
        # groups_mean = groups[val].filter(lambda x: x.mean() > threshold)
        # res = self.df.loc[groups_mean.index]
        # return res

        # Option B
        groups = self.df.groupby(group_col)
        groups_mean = groups[val].mean()
        filter = groups_mean > threshold
        true_group = groups_mean[filter]
        area_names = true_group.index.tolist()

        filter_rows = self.df[group_col].isin(area_names)
        res = self.df[filter_rows]
        return res


    # Q6
    def merge(self,left, right,col = "netVal"):
        pass
    def merge_sort(self,L,col = "netVal"):
      if

    # Q7
    def binary_search(self,d, low, high, x, col="netVal"):
        if high >= low:
            mid = (high + low) // 2

            if d[col].iloc[mid] == x:
                return mid

            if d[col].iloc[mid] > x:
                return self.binary_search(d, low, mid - 1, x, col)
            else:
                return self.binary_search(d, mid + 1, high, x, col)

        else:
            return low

def main():
    data = Data_Analyzer('import_export.csv')
    print(data)

    # Q1
    print(data.percent_nans())
    # Q2
    data.replace_nans()
    print(data.percent_nans())

    # Q3
    data.omit_zero_lines(colnames = ["import","export"])

    # Q4
    data.calc_diff("export", "import", "netVal")
    print(data.df.head())

    # Q5
    arr = data.flt(group_col = "Area",val="netVal", threshold=0)
    arr = arr[["Year","netVal"]].sort_values(by="netVal").reset_index(drop=True)
    # arr.to_csv("sorted_netVal.csv",index=False)
    # arr = pd.read_csv("sorted_netVal.csv")

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
