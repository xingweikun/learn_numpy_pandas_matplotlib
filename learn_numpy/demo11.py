import numpy as np
a=np.array([[[1,2],[4,5],[7,8]],[[8,9],[11,12],[14,15]],[[10,11],[13,14],[16,17]],[[19,20],[22,23],[25,26]]])
print(f'a:\n{a}')
print('a.shape:',a.shape)#0轴是行，1轴是列，2轴是纵深

print('*'*30)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'b:\n{b}')
print('b.shape:',b.shape)
print(b[0:2])
print(b[:2,1:])

print('*'*30)

c=np.arange(16).reshape((2,2,4))
print(f'c:\n{c}')
print(c.shape)