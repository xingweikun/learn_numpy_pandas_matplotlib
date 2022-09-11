import matplotlib.pyplot as plt
import squarify
import pandas as pd

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
数据 = pd.read_excel('./课件/29.树状图.xlsx')
自定义颜色 = ['r', 'y', 'b', 'g', 'yellow', 'cyan', 'coral']
图 = squarify.plot(sizes=数据.销售数量,  # 指定数据
                  label=数据.名称,  # 指定标签
                  color=自定义颜色,  # 自定义颜色
                  alpha=0.6,
                  value=数据.销售数量,  # 添加数据标签
                  edgecolor='white',  # 设置边界框颜色为白色
                  linewidth=3,  # 设置边框宽度
                  text_kwargs={'fontsize': 16})  # 设置字体大小
图.set_title("销售情况", fontdict={'fontsize': 20})
plt.axis('off')  # 去掉坐标轴
plt.tick_params(top='off', right='off')  # 去掉刻度
plt.show()