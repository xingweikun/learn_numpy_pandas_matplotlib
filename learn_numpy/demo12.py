import numpy as np
a=np.arange(24).reshape((4,6))
print(f'a:\n{a}')
print('行列转置:\n',a.transpose())

print('*'*30)

a=np.arange(24).reshape((4,6))
print('轴转置:\n',a.swapaxes(1,0))