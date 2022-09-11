import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False
数据 = pd.read_excel('./课件/28.瀑布图.xlsx')
列表 = np.arange(len(数据.金额), dtype=np.float64)
下面的距离 = 0
for i in 数据.金额.index:
    x = 列表[i]
    y = 数据.金额[i]
    if 数据.金额[i] >= 0:
        盈利 = plt.bar(x, y, 0.8, align='center', bottom=下面的距离, label="盈利", color='r')
    else:
        亏损 = plt.bar(x, y, 0.8, align='center', bottom=下面的距离, label="亏损", color='g')
    下面的距离 += y
    x += 0.8
plt.legend(handles=[盈利, 亏损])
plt.gca().yaxis.grid(True, linestyle='--', color='grey', alpha=.25)
日期 = [d.strftime('%Y-%m-%d') for d in 数据.日期]
plt.xticks(np.arange(len(数据.金额)), 日期, rotation=45)
plt.show()
