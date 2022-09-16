import random

# 如果不设置seed，则每次会生成不同的随机数。
# random.seed(10)
print(random.random())  # 用来随机生成一个0到1之间的浮点数，包括零。
print(random.random())

import numpy as np

one_wei = np.random.rand(3)
print('one_wei:\n', one_wei)
two_wei = np.random.rand(2, 3)
print('two_wei:\n', two_wei)
three_wei = np.random.rand(2, 3, 4)
print('three_wei:\n', three_wei)

print('*' * 30)

import matplotlib.pyplot as plt

# 绘制正弦曲线
x = np.linspace(-10, 10, 100)  # 在[-10,10]闭区间或半闭区间中，数量为100
# y=np.sin(x)#sin正弦,cos余弦
# 加入噪声
y = np.sin(x) + np.random.rand(len(x))  # 生成均匀分布，len(x轴)就是维度，相加就是定义元素的相加
plt.plot(x, y)
plt.show()
#
