import numpy as np

# 与np.random.shuffle(一维数组)效果一样,就是把一维数组重新排序了
a = np.random.permutation(10)  # 这里的10就看成是range(10)
print(a)
b = np.arange(9).reshape(3, 3)
print(np.random.permutation(b))
c = np.random.normal(1, 10, 10)  # 平均值1,方差10,10个数
print(c)
d = np.random.uniform(1, 10, 10)
print(d)
e = np.random.uniform(1, 10, (2, 3))
print(e)

print('*' * 30)

arr1 = np.arange(10)
print(arr1)
print(np.sqrt(arr1))  # 返回正的平方根
print(np.exp(arr1))  # 计算每个元素的自然指数值e的x次方

print('*' * 30)

x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print('--------')
print(y)
print('--------')
print(np.maximum(x, y))  # 对位比较大小，取大的，生成新的数组返回，逐个元素地将 x和 y 中元素的最大值计算出来
