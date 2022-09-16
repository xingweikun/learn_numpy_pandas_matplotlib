import numpy as np

a = np.arange(36).reshape(9, 4)
print(f'a:\n{a}')
print(a[[4, 3, 0, 6]])

print('*' * 30)

b = np.arange(32).reshape((8, 4))
print(b)
dq = b[[1, 5, 7, 2], [0, 3, 1, 2]]  # 取第1行第0列，第5行第3列，第7行第1列，第2行第2列
print(dq)

print('*' * 30)

c = np.arange(36).reshape(9, 4)
print(c[:, [1, 2]])  # 所有行的，第1,2列

print('*' * 30)

d = np.arange(10)
sy = np.array([[0, 2], [1, 3]])
print(f'd:{d}')
print(d[sy])

print('*' * 30)

e = np.random.randint(1, 100, 10)
print(e)
max_index = e.argsort()[-3:]
print(max_index)
print(e[max_index])
