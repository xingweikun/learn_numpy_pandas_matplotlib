import numpy as np

# lexsort(keys, axis=-1)
# lexsort()根据键值的字典序进行排序，支持对数组按指定行或列的顺序排序，间接排序，不修改原数组，返回索引。一般对一维数组使用argsort()。
# 默认按最后一行元素由小到大排序, 返回最后一行元素排序后索引所在位置。
x = np.array([[0, 12, 48], [4, 18, 14], [7, 1, 99]])
print(np.lexsort(x))
a = np.array([1, 5, 1, 4, 3, 4, 4])
b = np.array([9, 4, 0, 4, 0, 2, 1])
ind = np.lexsort((b, a))
print(ind)
print(list(zip(a[ind], b[ind])))
c = [[1, 5, 1, 4, 3, 4, 4], [9, 4, 0, 4, 0, 2, 1]]
print(np.lexsort(c))
print(x[np.lexsort(x.T)])  # 按最后一列顺序排序
print(x[np.lexsort(-x.T)])  # 按最后一列逆序排序
print(x[np.lexsort(x[:, ::-1].T)])  # 按第一列顺序排序
print(x.T[np.lexsort(x)].T)  # 按最后一行顺序排序
print(x.T[np.lexsort(x[::-1, :])].T)  # 按第一行顺序排序
