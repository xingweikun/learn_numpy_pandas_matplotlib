import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
数据 = pd.read_excel('./课件/09.折线与柱状组合图.xlsx')
布 = plt.figure()
图1 = 布.add_subplot(111)
图1.bar(数据.班级, 数据.销售量, label="销售量")
图1.legend(loc='upper left')
图1.set_ylim([0, 12500])
图1.set_ylim([0, 12500])
# twinx()表示共享x轴，同理twiny()表示共享y轴
图2 = 图1.twinx()
图2.plot(数据.班级, 数据.毛利率, 'or-', color='r', label='毛利率')
图2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=2))
图2.legend(loc='upper right')
图2.set_ylim([0, 1])
for x, y in zip(数据.班级, 数据.毛利率):
    plt.text(x, y, str(round(y * 100, 2)) + "%", color='b', fontsize=20)
plt.show()

# 第二种情况：已经是百分比
import matplotlib.ticker as mtick

布 = plt.figure()
图1 = 布.add_subplot(111)
图1.bar(数据.班级, 数据.销售量, label="销售量")
图1.legend(loc='upper left')
图1.set_ylim([0, 12500])
# twinx()表示共享x轴，同理twiny()表示共享y轴
图2 = 图1.twinx()
图2.plot(数据.班级, 数据.毛利率2, 'or-', color='r', label='毛利率')
图2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))
图2.legend(loc='upper right')
图2.set_ylim([0, 100])
for x, y in zip(数据.班级, 数据.毛利率2):
    plt.text(x, y, str(y) + '%', color='b', fontsize=20)
plt.show()
