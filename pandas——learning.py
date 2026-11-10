import pandas as pd
df = pd.read_csv(r"D:\AI_learning\data\scores.csv", encoding="utf-8")
print(df)
# print(df.shape)
# print(df.dtypes)
# print(df.head(5))
# print(df.columns)
# print(df.info())
# print(df.describe())
# assert df.shape == (8, 5)
df["total"] = df["math"] + df["english"] +df['chinese']
df['avg'] = df['total'] / 3
df['avg'] = df['avg'].round(2)
# df_sort = df.sort_values(by=['avg'], ascending=False)
# print(df_sort.head(5))
# df_sort.to_csv("data/scores_sorted.csv", index=False, encoding="utf-8-sig")
# assert df.loc[df["avg"].idxmax(), "name"] == "王五"
# assert df["avg"].max() == 91.33
df[df['avg'] >= 85]
df[(df['class']  == 'A' ) & (df['avg'] > 80)]
# print(df[df['name'].isin(['张三','李四'])])
# print(df[df['avg'].between(60,80)])
# print(df[df['name'].str.contains('张')])
# print(df.sort_values('avg',ascending=False))
df.sort_values(['class','avg'],ascending = [True,False])
# print(df.loc[2:4,['class','avg']])
# print(df.iloc[2:5,1:3])
df.loc[df['chinese'].idxmax(),'name']
df.query('`class` == "A" and avg > 80')
r = df[df["avg"] >= 85]
assert len(r) == 3
assert set(r["name"]) == {"王五", "孙八", "张三"}