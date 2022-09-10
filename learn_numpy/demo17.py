import numpy as np
a = np.array([1,2,3,4,3,5,3,6])
print(f'数组：{a}')
print('np.sum(a):',np.sum(a))
print('np.prod(a):',np.prod(a))
print('np.cumsum(a):',np.cumsum(a))   # 从0开始元素的累积和
print('np.cumprod(a):',np.cumprod(a))  # 从1开始元素的累积积
print('np.max(a):',np.max(a))
print('np.min(a):',np.min(a))
print('np.argmax(a):',np.argmax(a))    # 最大值所在的下标
print('np.argmin(a):',np.argmin(a))    # 最小值所在的下标
print('np.mean(a):',np.mean(a))      # 平均数
print('np.median(a):',np.median(a))    # 中位数
print('np.average(a):',np.average(a))   # 加权平均
counts = np.bincount(a) # 统计非负整数的个数，不能统计浮点数
print('np.argmax(counts):',np.argmax(counts)) # 返回众数,此方法不能用于二维数组
