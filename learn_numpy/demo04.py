import numpy as np

a = np.zeros(10, dtype=np.int32, order='C')
print(f'a:{a}')
b = np.zeros((2, 4))
print(f'b:\n{b}')

print('*' * 30)

a1 = np.array(
    [[0, 1, 2],
     [3, 4, 5]]
)
print(f'a1:\na{a1}')
a2 = np.zeros_like(a1)
print(f'a2:\n{a2}')
b1 = np.array([0., 1., 2.])
print(f'b1:{b1}')
b2 = np.zeros_like(b1)
print(f'b2:{b2}')

print('*' * 30)

c = np.full(3, 520)
print(f'c:{c}')
c1 = np.full((2, 4), 1314)
print(f'c1:\n{c1}')

print('*' * 30)

d1 = np.array(
    [[0, 1, 2],
     [3, 4, 5]])
print(f'd1:\n{d1}')
d2 = np.full_like(d1, 12)
print(f'd2:\n{d2}')
d3 = np.array([0., 1., 2.])
print(f'd3:\n{d3}')
d4 = np.full_like(d3, 20)
print(f'd4:\n{d4}')
