import pandas as pd
import numpy as np


class Data_Process():
    def __init__(self, fname):
        self.df = pd.read_csv(fname)

    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def modify_col(self, col):
        # Option A
        # self.df[col] = self.df[col].replace("Gold", 3)
        # self.df[col] = self.df[col].replace("Silver", 2)
        # self.df[col] = self.df[col].replace("Bronze", 1)
        # self.df[col] = self.df[col].fillna(0)

        # Option B
        replace_dict = {
            "Gold": 3,
            "Silver": 2,
            "Bronze": 1,
            np.NaN: 0
        }
        self.df[col] = self.df[col].replace(replace_dict)

    # Q2
    def replace_by_mean(self, group_cols, val):
        groups = self.df.groupby(group_cols)
        df_mean = groups[val].transform("mean")
        self.df[val] = self.df[val].fillna(df_mean)

        # Option B
        # groups = self.df.groupby(group_cols)
        #
        # frames = []
        # for i,g in groups:
        #     print(g)
        #     group_avg = g[val].mean()
        #     g[val] = g[val].fillna(group_avg)
        #     frames.append(g)
        #
        # new_df = pd.concat(frames)
        # new_df = new_df.sort_index()
        # self.df = new_df

    # Q3
    def data_select(self, cat_col, cat, num_col, threshold, cols):
        cat_filter = self.df[cat_col] == cat
        cat_rows = self.df[cat_filter]

        num_filter = cat_rows[num_col] >= threshold
        num_rows = cat_rows[num_filter]

        self.df = num_rows[cols]

        # Option B
        # self.df = self.df.loc[(self.df[cat_col] == cat) & (self.df[num_col] >= threshold), cols]
        return True

    # Q4
    def calc_counts(self, grps, val):
        groups = self.df.groupby(grps)

        columns = self.df[val].unique()
        indexes = groups.indices.keys() # get the names of the groups
        new_df = pd.DataFrame(columns=columns, index=indexes)

        for i,g in groups:
            group_value_count = g[val].value_counts()
            value_count_sum = group_value_count.sum()

            for c in columns:
                current_column_count = group_value_count.loc[c]
                calc_percentage = current_column_count / value_count_sum * 100
                new_df.loc[i, c] = calc_percentage

        return new_df


    # Q5
    def rename_index(self, d, new_colname):
        d.reset_index(inplace=True)
        d.rename(columns={"index": new_colname}, inplace=True)
        return d

    # Q6
    def selection_sort(self, d, col, ascending=False):
        n = d.shape[0]

        """"
        i = 0 -> num of rows 
        [30.0, 22.0, 21.0, 21.0, 21.0, 27.0, 22.0, 29.0, 34.0, 22.0, 26.0, 30.0, 34.0, 20.0, 25.0, 29.0, 33.0, 26.0, 30.0]
        """
        for i in range(n):
            min_index = i
            max_index = i
            """
            j = current row + 1 (i+1) -> num of rows 
            """
            for j in range(i+1, n):
                if not ascending:
                    if d[col].iloc[min_index] > d[col].iloc[j]:
                        min_index = j
                else:
                    if d[col].iloc[max_index] < d[col].iloc[j]:
                        max_index = j

            # min_index save the min value in column 'col'
            if not ascending:
                d.iloc[min_index], d.iloc[i] = d.iloc[i].copy(), d.iloc[min_index].copy()
            else:
                d.iloc[max_index], d.iloc[i] = d.iloc[i].copy(), d.iloc[max_index].copy()

            # Option B
            # temp = d.iloc[min_index].copy()
            # d.iloc[min_index] = d.iloc[i].copy()
            # d.iloc[i] = temp.copy()

        return d


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

    a = {"first": 1,
         "second": 2}

    for k,v in a.items():
        print(k)
        print(v)


