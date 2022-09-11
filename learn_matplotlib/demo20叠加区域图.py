import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('./课件/08.折线图.xlsx')
plt.plot(data.时间,data.蔬菜)
plt.plot(data.时间,data.水果)
'''
plt.fill_between(x, 0, y, facecolor='green', alpha=0.3)
参数：
x：第一个参数表示覆盖的区域，我直接复制为x，表示整个x都覆盖
0：表示覆盖的下限
y：表示覆盖的上限是y这个曲线
facecolor：覆盖区域的颜色
alpha：覆盖区域的透明度[0,1],其值越大，表示越不透明
'''
plt.fill_between(data.时间,0,data.蔬菜,facecolor='r',alpha=0.3)
plt.fill_between(data.时间,0,data.水果,facecolor='g',alpha=0.3)
plt.show()

# 两条曲线之间的面积填充
data = pd.read_excel('./课件/08.折线图.xlsx')
plt.plot(data.时间,data.蔬菜)
plt.plot(data.时间,data.水果)
plt.fill_between(data.时间,data.蔬菜,data.水果,facecolor='r',alpha=0.3)
plt.show()

# 高亮显示数据
import numpy as np
x=np.array([i for i in range(30)])
y=np.random.rand(30)
#设置想要高亮数据的位置
lists=[[1, 6],[10, 12],[20, 23], [26, 28]]
#画图
plt.plot(x,y,'r')
for i in lists:
    plt.fill_between(x[i[0]:i[1]],0,1,facecolor='r',alpha=0.3)
plt.show()