import pandas as pd
df = pd.read_csv('data/dirty.csv',encoding = 'UTF-8')
print(df)
raw = df.copy()
before_raws = len(raw)
before_missing = df.isnull().sum()
# print(df.isnull().sum())
# print(df.dropna(subset = ['score']))
# df['score'] = df['score'].fillna(df['score'].mean())  #score列取平均值填入空位，列中含有abc，列为字符串，无法取平均
# df['score'] = df['score'].astype(int)  #把score列的值转换为整数，NAN值本质为浮点数，不能转换
# df['name'] = df['name'].str.strip() #指定列首尾去空格
# df = df.drop_duplicates(subset=['id'])  #指定列去掉重复行
# df = df.rename(columns={'旧名':'新名'})  #对列重命名，大括号是字典格式：`'原来的列名' : '想要改成的新列名'`
df['name'] = df['name'].str.strip()  #第一题姓名去空格
df['score'] = pd.to_numeric(df['score'], errors = 'coerce') #第二题，字符串转化为空值

# df.loc[ df['class'] == 'A','score'] = df.loc[ df['class'] == 'A','score'].fillna(df.loc[ df['class'] == 'A','score'].mean())
# df.loc[ df['class'] == 'B','score'] = df.loc[ df['class'] == 'B','score'].fillna(df.loc[ df['class'] == 'B','score'].mean())#第三题，控制填入全班平均分
df = df.fillna(df.groupby('class')['score'].transform('mean'))
df = df.drop_duplicates(subset=['id'])
df = df.dropna(subset=['name'])
print(f'清洗前行数为：{before_raws}，清洗后行数为：{len(df)}')
print('\n清洗前各列缺失值为')
print(f'{before_missing.to_frame() }')
print('\n清洗后各列缺失值为')
print(f'{df.isnull().sum().to_frame()}')
print(df)