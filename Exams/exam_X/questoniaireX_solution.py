import pandas as pd
import numpy as np

class Data_Analyzer():
    def __init__(self,fname):
        self.df = pd.read_csv(fname)
    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def percent_nans(self):
        res = pd.Series(np.zeros(self.df.shape[1]),index=self.df.columns)
        for i in self.df.columns:
            res[i] = 100*sum(self.df[i].isna())/self.df.shape[0]
        return res

    # Q2
    def replace_nans(self):
        self.df.replace(np.NaN,0,inplace=True)
        return True

    # Q3
    def omit_zero_lines(self,colnames=["import","export"]):
        flt = np.any(self.df[colnames]!=np.zeros(len(colnames)),axis=1)
        self.df = self.df.loc[flt]
        return

    # Q4
    def calc_diff(self,col1,col2,newcol):
        def f(x,c1,c2):
            return pd.Series(x[c1] - x[c2])
        self.df[newcol] = self.df.apply(f,c1=col1,c2=col2,axis = 1)
        return

    # Q5
    def flt(self,group_col = "Area",val = "", threshold = 0):
        grp = self.df.groupby(group_col)
        f = grp[val].filter(lambda x: x.mean()>threshold) > threshold
        return self.df.loc[f.index]

    # Q6
    def merge(self,left, right,col = "netVal"):
        res = pd.DataFrame([])
        i_left, i_right = 0, 0
        while i_left < left.shape[0] and i_right < right.shape[0]:
            if left[col].iloc[i_left] < right[col].iloc[i_right]:
                res = res.append(left.iloc[i_left])
                i_left += 1
            else:
                res = res.append(right.iloc[i_right])
                i_right += 1
        if i_right < right.shape[0]:
            res = pd.concat([res,right.iloc[i_right:]])
        else:
            res = pd.concat([res,left.iloc[i_left:]])
        # print(f"merge: {left} \n&\n {right} \nto\n {res}")
        return res

    def merge_sort(self,L,col = "netVal"):
        # print(f"merge sort: {L}")
        if L.shape[0] ==1:
            return L.reset_index(drop=True)
        else:
            middle = L.shape[0] // 2
            left = self.merge_sort(L.iloc[:middle],col)
            right = self.merge_sort(L.iloc[middle:],col)
            return self.merge(left, right,col)

    # Q7
    def binary_search(self,d, low, high, x, col="netVal"):
        # Check base case
        if high >= low:
            mid = (high + low) // 2

            # If element is present at the middle itself
            if d[col].iloc[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left sub-array
            elif d[col].iloc[mid] > x:
                return self.binary_search(d, low, mid - 1, x,col)

                # Else the element can only be present in right subarray
            else:
                return self.binary_search(d, mid + 1, high, x,col)

        else:
            # Element is not present in the array, return the closest high boundary
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
