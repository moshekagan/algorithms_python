import pandas as pd
import numpy as np

class Data_Analyzer():
    def __init__(self,fname):
        self.df = pd.read_csv(fname)
    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def percent_nans(self):
      pass

    # Q2
    def replace_nans(self):
        pass

    # Q3
    def omit_zero_lines(self,colnames=["import","export"]):
        pass


    # Q4
    def calc_diff(self,col1,col2,newcol):
        pass


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
