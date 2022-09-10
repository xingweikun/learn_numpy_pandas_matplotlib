import numpy as np
a = np.array([3,6,7,9,2,1,8,5,4])
a.sort()
print(a)
b = np.array([[0,12,48],[4,18,14],[7,1,99]])
print(np.sort(b))#默认按最后的轴排序
print(np.sort(b,axis=0))#按行排序

print('*'*30)

x=np.array([59,29,39])
a=np.argsort(x)
print(f'索引升序:{a}')
print(f'数组升序:{x[a]}')
a=np.argsort(-x)
print(f'索引降序:{a}')
print(f'数组降序:{x[a]}')

x = np.array([[0, 12, 48], [4, 18, 14], [7, 1, 99]])
a1=np.argsort(x)
print(f'索引排序:\n{a1}')
print(np.array([np.take(x[i], x[i].argsort()) for i in range(3)]))