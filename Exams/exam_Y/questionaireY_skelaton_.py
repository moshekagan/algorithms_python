import pandas as pd
import numpy as np


class Data_Process():
    def __init__(self, fname):
        self.df = pd.read_csv(fname)

    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def modify_col(self, col):
        replacement_dict = {
            "Medal": {
                "Gold": 3,
                "Silver": 2,
                "Bronze": 1,
                np.NaN: 0
            }
        }
        self.df[col] = self.df[col].replace(replacement_dict[col])

    # Q2
    def replace_by_mean(self, group_cols, val):
        grouped_by = self.df.groupby(group_cols)

        frames = []
        for i,g in grouped_by:
            group_avg = g[val].mean()
            g[val] = g[val].replace(np.NaN, group_avg)
            frames.append(g)

        new_df = pd.concat(frames).sort_index()
        self.df = new_df

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
        indexes = groups.indices.keys()
        new_df = pd.DataFrame(index=indexes, columns=columns)

        for i,g in groups:
            group_value_count = g[val].value_counts()
            total_count = group_value_count.sum()

            for c in columns:
                current_column_count = group_value_count.loc[c]
                new_df.loc[i, c] = current_column_count / total_count * 100

        return new_df

        # Option B - from ChatGPT
        # # חישוב כמות המופעים עבור כל קבוצה בעמודה val
        # count_series = self.df.groupby(grps)[val].value_counts()
        #
        # # חישוב סך הכל של כל קבוצה
        # total_counts = count_series.groupby(level=grps).sum()
        #
        # # חישוב האחוזים
        # percentage_df = (count_series / total_counts) * 100
        #
        # # המרת הסדרה לטבלת DataFrame
        # percentage_df = percentage_df.unstack(fill_value=0)
        #
        # return percentage_df

    # Q5
    def rename_index(self, d, new_colname):
        d[new_colname] = d.index
        d = d.reset_index(drop=True)
        return d

    # Q6
    def selection_sort(self, d, col, ascending=False):
        rows = d.shape[0]

        for i in range(rows):
            min_max_index = i
            for j in range(i+1, rows):
                if ascending:
                    if d[col][j] < d[col][min_max_index]:
                        min_max_index = j
                else:
                    if d[col][j] > d[col][min_max_index]:
                        min_max_index = j

            # swap
            temp = d.iloc[min_max_index].copy()
            d.iloc[min_max_index] = d.iloc[i].copy()
            d.iloc[i] = temp.copy()

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
