import matplotlib.pyplot as plt
import pandas as pd
import pandas_W3D5 as pdw
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(8,5))
df = pd.read_csv('data/sales.csv',encoding='UTF-8')
df = pdw.clean(df)
s = df.groupby('category')['amount'].sum()
s = s.sort_values(ascending=False)
x = s.index
height = s.values
bars_1 = ax.bar(x,height,align='center',color='#4C78A8')  #柱状图，h 高度  ax.barh(y,width)横向条状图
ax.bar_label(bars_1,fmt='%.0f')
ax.set_xlabel('品类')
ax.set_ylabel('销售额（元）')
ax.set_title('各品类销售额统计表')
ax.set_ylim(0,height.max()*1.2)
ax.yaxis.set_major_formatter(lambda v,p: f'{v:,.0f}')
fig.savefig('charts/02_category.png',dpi=150,bbox_inches='tight')
plt.close(fig)
fig, ax = plt.subplots(figsize=(8,5))
a = df.groupby('city')['amount'].sum().sort_values(ascending=False)
y = a.index
width = a.values
bar_2 = ax.barh(y,width,align='center',color='#4C78A8')
ax.invert_yaxis()  #y轴翻过来
ax.bar_label(bar_2,fmt='%.0f')
ax.set_ylabel('城市')
ax.set_xlabel('销售额（元）')
ax.set_title('各城市销售额统计表')
ax.set_xlim(0,width.max()*1.2)
ax.xaxis.set_major_formatter(lambda v,p: f'{v:,.0f}')
fig.savefig('charts/03_city.png',dpi=150,bbox_inches='tight')
plt.close(fig)
from pathlib import Path
for f in ("charts/02_category.png", "charts/03_city.png"):
    assert Path(f).stat().st_size > 10_000, f
print('全部通过')

