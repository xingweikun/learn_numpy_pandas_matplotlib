import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
数据 = pd.read_excel('./课件/30.玫瑰图.xlsx')
角度 = np.linspace(0, 2 * np.pi, len(数据.业绩), endpoint=False)
图 = plt.axes(polar=True)  # 实例化极坐标系
# 图.set_theta_direction(-1) # 顺时针为极坐标正方向
图.set_theta_zero_location('N')  # 让0度指向N
列表 = np.random.random((len(数据.业绩)))
颜色 = ['b', 'gold', 'darkviolet', 'turquoise', 'r', 'g', 'grey', 'c', 'm', 'y', 'k', 'darkorange', 'lightgreen', 'plum','tan']
业绩 = np.concatenate((数据.业绩, [数据.业绩[0]]))
角度 = np.concatenate((角度, [角度[0]]))
姓名 = np.concatenate((数据.姓名, [数据.姓名[0]]))
plt.bar(角度, 业绩, width=0.33, color=颜色)
plt.bar(x=角度, height=130, width=0.33, color='white')  # 挖孔
# 数据标签
for 角度, 业绩, 姓名 in zip(角度, 业绩, 姓名):
    plt.text(角度 + 0.03, 业绩 + 100, str(姓名))
plt.gca().set_axis_off()
plt.show()