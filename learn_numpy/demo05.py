import numpy as np
a=np.random.randn()
print(f'一个随机数:{a}')
b=np.random.randn(3)
print(f'三个数:{b}')
c=np.random.randn(3,2)
print(f'3行2列:\n{c}')
d=np.random.randn(3,2,4)
print(f'3块，每块是2行4列:\n{d}')
print('四舍五入(保留两位小数):',np.round(3.14159,2))

print('*'*30)
a = np.array(range(1,8),dtype=float)       # 修改数据类型
b = np.array(range(1,8),dtype='float32') # 修改数据类型和位数
print(a)
print(b)
print(a.dtype)
print(b.dtype)
print(type(a))
print(type(b))