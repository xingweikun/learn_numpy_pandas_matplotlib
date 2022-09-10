import numpy as np
a=np.arange(10).reshape(2,5)
b=a.reshape(10)
c=a.flatten()
print(f'a:{a}\nb:{b}\nc:{c}')#不清楚对方什么阵型，直接转一维
# a.reshape(1,10)等于a.reshape(10)

print('*'*30)

print(a+1,'\n',a*3)
b=np.random.randn(2,5)
print(a+b,'\n',a-b)
c=np.arange(6)
d=np.arange(24).reshape(4,6)
print(f'c:{c}\nd:\n{d}\nd-c:\n',d-c)