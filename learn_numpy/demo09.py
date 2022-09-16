import numpy as np

a = np.arange(10)
print('a:', a)
tj = a > 5
print(f'tj:{tj}')
print(a[tj])

a[a <= 5] = 0
a[a > 5] = 1
print(f'a:{a}')
a = np.arange(10)
a[a > 5] += 520
print(f'a:{a}')

print('*' * 30)

b = np.arange(1, 21).reshape(4, 5)
print(f'b:{b}')
tj = b > 10
print(b[tj])

print('*' * 30)

print(b[:, 3])
tj = b[:, 3] > 5
print(tj)
b[tj] = 520
print(b)

print('*' * 30)

c = np.array([[10, 20, 30], [50, 40, 10], [10, 1, 10]])
print(c)
tj = c > 25
print(tj)
print(c[tj])

d = np.arange(10)
print(d[(d % 2 == 0) | (a < 7)])
