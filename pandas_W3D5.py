import pandas as pd
def load(path):
    raw = pd.read_csv(path, encoding='UTF-8')
    return raw

def clean(raw):
    df = raw.drop_duplicates(subset=['order_id'])
    df_columns = df.columns
    df = df.dropna(subset = df_columns[:])
    # print(df.isnull().sum())
    # print(df.duplicated().sum())
    # print(df.shape)
    df['qty'] =df['qty'].astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors = 'coerce')
    df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
    df['amount'] = df['qty']*df['unit_price']
    df['profit'] = df['amount'] -df['qty'] * df['cost']
    print(raw.dtypes)
    print(df['amount'].sum())
    return df
def analyze(raw,df):
    df_cateamount = df.groupby('category')['amount'].sum()
    df_cateamount = df_cateamount.sort_values(ascending = False)
    print(df_cateamount.head(3))
    df['month'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')
    df_monamount = df.groupby('month')['amount'].sum()
    df_maxmonamount = df_monamount.idxmax()
    df_minmonamount = df_monamount.idxmin()
    print(df_monamount)
    print(f'最高月为{df_maxmonamount},最低月为{df_minmonamount}。')
    df_top10 = df.sort_values('amount',ascending = False)
    df_top10 = df_top10.nlargest(10,'amount')
    df_top10 = df_top10.reset_index(drop = True)
    df_top10 = df_top10.drop(columns = ['date','channel','qty','unit_price','cost','profit','month'])
    print(df_top10)
    df_channel = df.groupby('channel')['amount'].mean().round(2)
    diff = df_channel['线上']-df_channel['门店']
    pct = diff / df_channel['门店'] * 100
    print(f'差额{diff.round(2)}，百分比{pct.round(2)}%')
    print(df_channel)
    overview = {
            '原始行数' : len(raw),
            '去重数' : int(raw['order_id'].duplicated().sum()),
            '清洗后行数' : len(df),
            '缺失分布' : {k : int(v) for k , v in df.isnull().sum().items() if v>0}
    }
    return {
        "overview": overview,
        "by_category":df_cateamount,
        "by_month": df_monamount,
        "top10":df_top10,
        "by_channel":df_channel,
    }
def report(results, path):
    ov  = results["overview"]
    cat = results["by_category"]      # Series，已按金额降序
    mon = results["by_month"]         # Series，索引是 "2026-01"
    top = results["top10"].iloc[0]    # 第一行，是个 Series
    ch  = results["by_channel"]       # Series，索引是 线上/门店

    gap = ch["线上"] - ch["门店"]

    lines = [
        "# 销售分析报告 2026-01 ~ 2026-06",
        f"- 原始 {ov['原始行数']} 行，去重 {ov['去重数']} 条，清洗后 {ov['清洗后行数']} 行进入分析。",
        f"- {cat.index[0]} 销售额 {cat.iloc[0]:,.0f}，占 {cat.iloc[0] / cat.sum():.0%}，"
        f"是第二名 {cat.index[1]} 的 {cat.iloc[0] / cat.iloc[1]:.2f} 倍。",
        f"- 6 个月里 {mon.idxmax()} 最高（{mon.max():,.0f}），{mon.idxmin()} 最低（{mon.min():,.0f}）。",
        f"- 单笔金额最高 {top['amount']:,.0f}：订单 {top['order_id']}，{top['city']} / {top['category']}。",
        f"- 线上客单价 {ch['线上']:,.0f}，门店 {ch['门店']:,.0f}，"
        f"线上比门店高 {gap:,.0f}（{gap / ch['门店']:+.0%}，基准=门店）。",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")



if __name__ == "__main__":
    raw = load("data/sales.csv")
    df = clean(raw)
    r = analyze(raw, df)

    assert len(raw) == 123                    # 数据事实
    assert len(df) == 112                     # 数据事实
    assert df["order_id"].duplicated().sum() == 0
    assert df[["city", "unit_price"]].isnull().sum().sum() == 0
    assert {"amount", "profit"} <= set(df.columns)
    assert abs(df["amount"].sum() - 799146) < 1

    assert r["by_category"].index[0] == "电脑"
    assert len(r["by_category"]) == 5
    assert len(r["by_month"]) == 6
    assert len(r["top10"]) == 10
    assert r["top10"]["amount"].is_monotonic_decreasing
    assert set(r["by_channel"].index) == {"线上", "门店"}
    assert set(r["overview"]) == {"原始行数", "去重数", "清洗后行数", "缺失分布"}

    print("通过")
    report(r, "report.md")