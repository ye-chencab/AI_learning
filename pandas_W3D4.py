import pandas as pd
df = pd.read_csv('data/scores_sorted.csv ',encoding='UTF-8')
df1 = pd.read_csv('data/classes.csv ',encoding='UTF-8')
# df.groupby('class')['score'].mean()  #按class分组，分别算出每个班 score的平均分
# df.groupby('class').agg({'score':['mean','max','count']})  #按班级分组，分别算出score列的平均值、最大值与人数
# df['class'].value_counts()    #统计每个班级出现的次数
# pd.pivot_table(df,index='class',values='score',aggfunc='mean')  #制作透视表函数，按class一行一行索引，让score列按mean函数执行
# pd.merge(students,scores,on='id',how='left') #how:left/right/inner/outer  #merge 合并函数。 st跟sc是需要合并的两张表，分为左跟右
#             #on='id'意为以id为合并列，两张表都得有id列，how的四个函数 L表示以左表主表，右表接上，空值填NAN，左表没有的删掉，R相反，IN选择交叉皆有的，OU为全合并
# pd.concat([df1,df2],ignore_index=True)  #表格上下合并，列尽量对齐，ig表示重新对行进行编号
# df['name'] = df['name'].str.strip()
# df['score'] = pd.to_numeric(df['score'],errors='coerce')   #to_numeric 函数专门用来把字符串或文本转化为数值，如果转换失败，则转化为coerce(NaN),raise(程序报错），ignore（保持原样不变）
# df['score'] = df['score'].fillna(df.groupby('class')['score'].transform('mean'))
# df = df.drop_duplicates(subset=['id'])
# df = df.dropna(subset=['name'])
print(df)
#每班的平均分、人数、最高分（一张表出结果）
# print(df.groupby('class').agg({'avg':['mean','count','max']}))
g=df.groupby('class').agg(人数=('name','count'),平均分=('avg','mean'),最高分=('avg','max'))
#每个班里平均分最高的那个人
dfmax = df.groupby('class')['avg'].idxmax()
best = df.loc[dfmax]
#把班主任表拼进来
df_hebing = pd.merge(df,df1,on='class',how='left')
#每位老师带的学生平均分
teacher_stat = df_hebing.groupby('teacher')['avg'].mean()
#表格上下合并
top4 = df.iloc[0:4]  #按位置取行列，df.iloc[0, 1] # 第0行，第1列   df.loc[0, 'score'] # 索引0这一行，score列
bottom4 = df.iloc[4:]
combined = pd.concat([top4,bottom4],ignore_index=True)
if __name__ == "__main__":
    assert set(g.index) == {"A", "B", "C"}
    assert list(g.columns) == ["人数", "平均分", "最高分"]
    assert g.loc["A", "人数"] == 3
    assert g.loc["C", "人数"] == 2
    assert abs(g.loc["B", "最高分"] - 91.33) < 0.01
    assert abs(g.loc["A", "平均分"] - 74.89) < 0.01

    assert len(best) == 3
    assert set(best["name"]) == {"张三", "王五", "孙八"}

    assert "teacher" in df_hebing.columns
    assert len(df_hebing) == len(df)
    assert df_hebing["teacher"].isnull().sum() == 0

    assert abs(teacher_stat.loc["张老师"] - 85.83) < 0.01

    assert len(combined) == len(df)
    assert combined["name"].iloc[0] == df["name"].iloc[0]

    print("全部通过")