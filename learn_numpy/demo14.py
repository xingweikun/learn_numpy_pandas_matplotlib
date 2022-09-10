import numpy as np
a=np.random.randint(3)
b=np.random.randint(1,10)
c=np.random.randint(1,10,size=(5,))
d=np.random.randint(1,20,size=(3,4))
e=np.random.randint(1,20,size=(2,3,4))
print(f'随机0~3:{a}\n随机1~10:{b}\n随机1~10取5个元素:{c}')
print(f'随机1~20取12个元素组成二维数组:\n{d}')
print(f'随机1~20取24个元素组成三维数组:\n{e}')

print(f'*'*30)

#0.0~1.0的随机数
one_w=np.random.random(3)
two_w=np.random.random(size=(2,3))
three_w=np.random.random(size=(3,2,3))
print(f'one_w:{one_w}\ntwo_w:\n{two_w}\nthree_w:\n{three_w}')
