import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
data = pd.read_excel('./课件/09.折线与柱状组合图.xlsx')
# 生成一个新图片
布 = plt.figure()
# 在这张图上做一个2*2（最多4个图）
one = 布.add_subplot(2, 2, 1)
two = 布.add_subplot(2, 2, 2)
three = 布.add_subplot(2, 2, 3)
plt.plot(data.班级, data.毛利率, label='毛利率', color='r', marker='*', ms=10)
four = 布.add_subplot(2, 2, 4)
plt.bar(data.班级, data.销售量, color='r', label='销售量', alpha=0.6)
plt.savefig('./图片/画布与子图.jpg')
plt.show()
