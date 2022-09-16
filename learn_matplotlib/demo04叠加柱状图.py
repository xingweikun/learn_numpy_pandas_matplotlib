import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('./课件/04.堆叠柱状图.xlsx')
plt.bar(np.arange(9), data['语文'], color="red", label="语文", align='center')
plt.bar(np.arange(9), data['数学'], bottom=data['语文'], color="green", label="数学", align='center')
plt.bar(np.arange(9), data['英语'], bottom=data['语文'] + data['数学'], color="yellow", label="英语", align='center')
# 设置x轴标签
plt.xticks(np.arange(9), data['姓名'])
# 显示图例，上面中心位置，分成3列
plt.legend(loc='upper center', ncol=3)
# 设置y轴的刻度范围
plt.ylim([0, 300])
for x1, y1 in enumerate(data['语文']):
    plt.text(x1, y1 - 10, str(y1), ha='center', fontsize=20, color='black')
for x2, y2 in enumerate(data['语文'] + data['数学']):
    plt.text(x2, y2 - 10, str(y2), ha='center', fontsize=20, color='black')
for x3, y3 in enumerate(data['语文'] + data['数学'] + data['英语']):
    plt.text(x3, y3 - 10, str(y3), ha='center', fontsize=20, color='black')
plt.grid()  # 网格线
plt.savefig('./图片/叠加柱状图.jpg')
plt.show()
