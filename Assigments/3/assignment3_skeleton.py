import pandas as pd
import numpy as np

class Data_Analyzer():
    def __init__(self,fname):
        self.df = pd.read_csv(fname)

    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def omit_zeros(self):
        pass

    # Q2
    def calc_total(self):
        def f(): # add input
            pass
        pass

    # Q3
    def select_group(self):
        pass

    # Q4
    def summ_by_group(self):
        pass

    # Q5
    def concat_dfs(self):
        pass

    # Q6
    def merge(self):
        pass

    def merge_sort(self):
        pass

def main():
    data = Data_Analyzer('employment.csv')
    print(data)

    # Q1
    # data.omit_zeros(colnames = ["Gender", "Salary","Bonus %"])
    # print(data.df.shape)
    # print(sum(data.df["Gender"]==0))
    # print(sum(data.df["Salary"]==0))
    # print(sum(data.df["Bonus %"]==0))

    # Q2
    ### in case Q1 didn't work, reload df using next line:
    # data.df = pd.read_csv("clean_df.csv")
    ### test calc_total:
    # data.calc_total("Salary", "Bonus %", "total")
    # print(data)
    # print(np.all(np.round((data.df.loc[:,"Salary"]*(1+(data.df.loc[:,"Bonus %"]/100))),1)==np.round(data.df.loc[:,"total"],1)))

    # Q3
    # females_salaries = data.select_group(group_col = "Gender", group = "Female")
    # males_salaries = data.select_group(group_col="Gender", group="Male")
    # print(females_salaries.shape)
    # print(males_salaries.shape)

    # Q4
    # females_salaries = data.summ_by_group(females_salaries,group_cols = ["Team"],val_col = ["total"],funcs = [np.mean])
    # print(females_salaries.shape)
    # print(females_salaries)
    # males_salaries = data.summ_by_group(males_salaries,group_cols = ["Team"],val_col = ["total"],funcs = [np.mean])
    # print(males_salaries.shape)
    # print(males_salaries)

    # Q5
    ### in case Q4 didn't work, use next line
    # females_salaries = pd.read_csv("females_salaries.csv")
    # males_salaries = pd.read_csv("males_salaries.csv")
    ### test concat_dfs:
    # join_dfs = data.concat_dfs([females_salaries,males_salaries],col1="females",col2="males",newcol = "diff")
    # print(join_dfs.shape)
    # print(join_dfs)

    # Q6
    ### in case Q5 didn't work, use next line
    # join_dfs = pd.read_csv("join_dfs.csv")
    ### test merge_sort:
    # arr = data.merge_sort(join_dfs,"diff").reset_index(drop=True)
    # print(arr)

if __name__=="__main__":
    main()
