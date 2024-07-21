import pandas as pd
import numpy as np


class Data_Process():
    def __init__(self, fname):
        self.df = pd.read_csv(fname)

    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def modify_col(self, col):
        pass

    # Q2
    def replace_by_mean(self, group_cols, val):
        pass

    # Q3
    def data_select(self, cat_col, cat, num_col, threshold, cols):
        pass

    # Q4
    def calc_counts(self, grps, val):
        pass

    # Q5
    def rename_index(self, d, new_colname):
        pass

    # Q6
    def selection_sort(self, d, col, ascending=False):
        pass


def main():
    data = Data_Process('athletes_short.csv')
    print(data)

    # Q1
    data.modify_col("Medal")
    print(data)
    # data.df.to_csv("post_Q1.csv",index=False)

    # Q2
    # data.df = pd.read_csv("post_Q1.csv")
    data.replace_by_mean(["Gender", "Team"], val="Height")
    data.replace_by_mean(["Gender", "Team"], val="Weight")
    data.replace_by_mean(["Gender", "Team"], val="Age")
    print(data.df.iloc[17:25])
    # data.df.to_csv("post_Q2.csv",index=False)

    # Q3
    # data.df = pd.read_csv("post_Q2.csv")
    data.data_select("Gender", "F", "Year", 2000, ["Team", "Year", "Medal"])
    print(data.df.shape)
    print(data)
    # data.df.to_csv("post_Q3.csv",index=False)

    # Q4
    # data.df = pd.read_csv("post_Q3.csv")
    female_scores = data.calc_counts(grps=["Team"], val="Medal")
    print(female_scores)
    # female_scores.to_csv("female_scores.csv",index=False)

    # Q5
    # female_scores = pd.read_csv("female_scores.csv")
    female_scores = data.rename_index(female_scores, "Country")
    print(female_scores)
    # female_scores.to_csv("post_Q5.csv",index=False)

    # Q6
    # female_scores = pd.read_csv("post_Q5.csv")
    print(data.selection_sort(female_scores, 3, ascending=False))
    print(data.selection_sort(female_scores, 3, ascending=True))


if __name__ == "__main__":
    main()
