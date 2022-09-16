import numpy as np

a = np.array([[1, 3, 6], [9, 3, 2], [1, 3, 4]])
print(np.sum(a, axis=0))  # 每行中的每个对应元素相加，返回一维数组
print(np.sum(a, axis=1))  # 每列中的每个元素相加，返回一维数组
print('a>3:', a > 3)
print(np.where(a > 3, 520, 1314))

print('*' * 30)

b = np.array([[1, 3, 6], [9, 3, 2], [1, 3, 4]])
print((a > 3).sum())  # 数组中大于3的数有几个
c = np.array([False, False, True, False])
print(c.any())
print(c.all())
