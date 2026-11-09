import pandas as pd
df = pd.read_csv(r"D:\AI_learning\data\scores.csv", encoding="utf-8")
print(df)
# print(df.shape)
# print(df.dtypes)
# print(df.head(5))
# print(df.columns)
# print(df.info())
print(df.describe())
assert df.shape == (8, 5)
df["total"] = df["math"] + df["english"] +df['chinese']
df['avg'] = df['total'] / 3
df['avg'] = df['avg'].round(2)
df_sort = df.sort_values(by=['avg'], ascending=False)
print(df_sort.head(5))
df_sort.to_csv("data/scores_sorted.csv", index=False, encoding="utf-8-sig")
assert df.loc[df["avg"].idxmax(), "name"] == "王五"
assert df["avg"].max() == 91.33