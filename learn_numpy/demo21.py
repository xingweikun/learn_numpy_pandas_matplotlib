import numpy as np
#去重
name = np.array(['张三','李四','张三','王五','张三','李四'])
print(np.unique(name))
a = np.array([1,3,1,3,5,3,1,3,7,3,5,6])
print(np.unique(a))
#检查一个数组中的值是否在另外一个数组中，并返回一个布尔数组：
a = np.array([6,0,0,3,2,5,6])
print(np.in1d(a,[2,3,6]))