import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_excel('./课件/08.折线图.xlsx')
# plt.plot(data.时间,data.蔬菜,label='蔬菜',color='r',marker='*',ms=10)
plt.plot(data.时间[:3], data.蔬菜[:3], label='蔬菜', color='r', marker='*', ms=10)
plt.plot(data.时间[2:], data.蔬菜[2:], label='蔬菜', color='b', marker='*', ms=10)
plt.plot(data.时间, data.水果, label='水果', color='g', marker='o', ms=10)
plt.plot(data.时间, data.食品, label='食品', color='b', marker='v', ms=10)
plt.plot(data.时间, data.用品, label='用品', color='y', marker='^', ms=10)
for y in [data.蔬菜, data.水果, data.食品, data.用品]:
    for x, y in zip(data.时间, y):
        plt.text(x, y + 3, str(y), ha='center', va='center', fontsize=20, rotation=0)
plt.savefig('./图片/折线图.jpg')
plt.show()
