import numpy as np
a = np.array([1,2,3,4,5,6])
b = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
print(a)
print(b)
print(a.shape)  # 返回一个元组，查看矩阵或者数组的维数(有几个数就是几维),就是几乘几的数组
print(b.shape)
print(a.ndim)   # 返回数组维度数目
print(b.ndim)
print(a.size)   # 返回数组中所有元素的数目
print(b.size)
print(a.dtype)  # 返回数组中所有元素的数据类型
print(b.dtype)