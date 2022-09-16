'''
极点：以圆的中心作为极点O，
极轴：以0°的方向引一条射线极轴Ox,
极径：选定一个长度单位r
极角：以Ox正方向开始计算角度θ（通常取逆时针方向）
极坐标：以极点O作为圆心，以极昼Ox的方向作为起点，以极径r作为半径，画一个以极角θ的扇形，最终圆规脚定的位置就是极坐标M
'''
import matplotlib.pyplot as plt

plt.polar()  # 空白极地图
plt.show()

import numpy as np

plt.polar(0.25 * np.pi, 20, 'ro')
plt.ylim(0, 100)
plt.show()

# 给定多个极角和极轴的时候
# 角度=np.array([0.25,0.75,1,1.5])
角度 = np.array([0.25, 0.75, 1, 1.5, 0.25])
# 极轴=[20,60,40,80]
极轴 = [20, 60, 40, 80, 20]  # 构造一个极坐标点，和第一个点重叠
# plt.polar(角度*np.pi,极轴,'ro')
plt.polar(角度 * np.pi, 极轴, 'ro-')  # 将每个点连线
# 填充颜色
plt.fill(角度 * np.pi, 极轴, 'r', alpha=0.75)
plt.ylim(0, 100)
plt.show()

import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# 使用ggplot的风格绘图
plt.style.use('ggplot')
data = pd.read_excel('./课件/22.雷达图.xlsx', index_col='姓名')
条件1 = "姓名=='A01'"
条件2 = "姓名=='A02'"
A01 = data.query(条件1)['分数']
A02 = data.query(条件2)['分数']
科目 = data.query(条件1)['科目']
# 设置雷达图角度，用于平分切开一个平面 linspace(起始，结束，len(A01)个等步长的样本数量，endpoint不包括结束值)
角度 = np.linspace(0, 2 * np.pi, len(A01), endpoint=False)
# 使雷达图封闭起来
A01 = np.concatenate((A01, [A01[0]]))
# print(A01)
A02 = np.concatenate((A02, [A02[0]]))
角度 = np.concatenate((角度, [角度[0]]))
科目 = np.concatenate((科目, [科目[0]]))
# 画图
布 = plt.figure()
图 = 布.add_subplot(111, polar=True)
图.plot(角度, A01, 'o-', linewidth=2, alpha=0.25, label='A01同学')  # linewidth线粗
图.fill(角度, A01, 'r', alpha=0.25)
图.plot(角度, A02, 'o-', linewidth=2, alpha=0.25, label='A02同学')  # linewidth线粗
图.fill(角度, A02, 'b', alpha=0.25)
# 标签
图.set_thetagrids(角度 * 180 / np.pi, 科目)
图.set_ylim(0, 100)
plt.legend(loc='best')
plt.show()
