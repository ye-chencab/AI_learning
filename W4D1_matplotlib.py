import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  #字体设置为微软雅黑，不设置字体中文会乱码
# plt.rcParams['axes.unicode_minus'] = False   #负号能正常显示
# fig , ax = plt.subplots(figsize = (8,5))
# #'fig' 整张画布  ‘ax’ 画布内坐标系  figsize = (8,5)画布大小，单位是**英寸**，宽 8 英寸、高 5 英寸
# ax.plot(x,y,marker ='o') # x,y 坐标值，‘o' 数据表示
# ax.set_title('标题')
# ax.set_xlabel('月份')   #x轴下方名称
# ax.set_ylabel('销售额（元）')
# fig.savefig('charts/01_monthly.png',dpi=150,bbox_inches='tight')  #dpi 清晰度  bbox_inches='tight' 自动裁切多余白框
# plt.close(fig)  #关掉该图纸
from pathlib import Path
import pandas as pd
df = pd.read_csv('data/sales.csv',encoding = 'utf-8')

df = df.drop_duplicates(subset = 'order_id')
df_columns = df.columns
df = df.dropna(subset = df_columns[:])

df['month'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')

df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
df = df.dropna(subset = ['qty','unit_price','cost'])
df['qty'] = df['qty'].astype(int)
df['amount'] = df['qty']*df['unit_price']
df_monthsum = df.groupby('month')['amount'].sum()
print(df_monthsum)
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  #字体设置为微软雅黑，不设置字体中文会乱码
plt.rcParams['axes.unicode_minus'] = False   #负号能正常显示
fig,ax = plt.subplots(figsize=(8,5))
x = df_monthsum.index#序列’索引‘
y = df_monthsum.values #序列’值‘
ax.plot(x,y,marker ='o',lw=2, color="#4C78A8")
# linewith 的简写  ，色号
ax.set_title("2026 上半年月度销售额", fontsize=14)# 字体大小
ax.set_xlabel('月份')
ax.set_ylabel('销售额（元）')
ax.set_ylim(0, df_monthsum.max() * 1.2)  #y轴从0开始起注，最大值再往上扩，给标题留空间
ax.grid(axis="y", ls="--", alpha=0.4)
# - `axis="y"`：只画横向网格线（跟着 Y 轴刻度走），不画竖线；写 `axis="both"` 就是横竖都有
# - `ls="--"`：`linestyle` 的简写，线型是虚线；`"-"`实线、`":"`点线
# - `alpha=0.4`：透明度，0~1，越小越淡
ax.yaxis.set_major_formatter(lambda v, p: f"{v:,.0f}")
# - 作用：Y 轴金额加上**千位分隔逗号**，比如 `157684` → `157,684`，可读性更好
# - `v`：刻度原始数值；`p` 是位置参数（固定带着就行，不用管）
# - `:,.0f`：逗号分隔、保留 0 位小数（整数）
max_val = df_monthsum.max()
max_month = df_monthsum.idxmax() #最大值索引
ax.annotate(
    f'最高：{max_val:.0f}元',
    xy=(max_month, max_val),
    xytext=(50, 10),
    textcoords="offset points",ha="center", fontsize=10,
    arrowprops=dict(arrowstyle="->", color='red',lw=1),
)
Path("charts").mkdir(exist_ok=True)
fig.savefig("charts/01_monthly.png", dpi=150, bbox_inches="tight")
plt.close(fig)
p = Path("charts/01_monthly.png")
assert p.exists(), "图没生成"
assert p.stat().st_size > 10_000, "图太小，可能是空白"
assert len(df_monthsum) == 6, "月份数不对"
assert df_monthsum.index.is_monotonic_increasing, "月份没排序"
assert (df["amount"] == df["qty"] * df["unit_price"]).all(), "amount 算错了"
print("通过")