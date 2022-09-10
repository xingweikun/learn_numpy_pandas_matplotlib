import numpy as np
a1=np.arange(5)
print(f'a:{a1}')
a2=np.arange(1,10,2)
print(f'a2:{a2}')

print('*'*30)

#order : {‘C’, ‘F’}, 可选规定返回数组元素在内存的存储顺序
b1=np.ones(3,dtype=np.float64,order='C')
print(f'b1:{b1},',b1.dtype)
b2=np.ones((2,3))
print(f'b1:\n{b2}')
b3=np.ones((5,))
print(f'b3:{b3}')

print('*'*30)

#np.ones_like(a,dtype=float,order='C',subok=True)
#subok ： bool，可选。True：使用a的内部数据类型，False：使用a数组的数据类型，默认为True
x=np.array(
    [[0,1,2],
    [3,4,5]]
)
print(f'x:\n{x}')
x1=np.ones_like(x)
print(f'x1:\n{x1}')
y=np.array([0,1,2])
print(f'y:{y}')
y1=np.ones_like(y)
print(f'y1:{y1}')