import numpy as np
a = np.random.choice(5,3)
print(f'从range(5)中拿随机数，生成只有3个元素的一维数组是：{a}')
b = np.random.choice(5,(2,3))
print(f'从range(5)中拿随机数，生成2行3列的数组是：\n{b}')
c = np.random.choice([1,2,9,4,8,6,7,5],3)
print(f'从[1,2,9,4,8,6,7,5]数组中拿随机数，3个元素：{c}')
d = np.random.choice([1,2,9,4,8,6,7,5],(2,3))
print(f'从[1,2,9,4,8,6,7,5]数组中拿随机数，生成2行3列的数组是：\n{d}')

print('*'*30)

one_w=np.arange(10)
print(f'没有随机排列前的一维数组:{one_w}')
np.random.shuffle(one_w)
print(f'随机排列后的一维数组:{one_w}')

two_w=np.arange(20).reshape(4,5)
print(f'没有随机排列前的二维数组:\n{two_w}')
np.random.shuffle(two_w)
#多维数组随机排列只按行随机，列是不变的
print(f'随机排列后的二维数组:\n{two_w}')

three_w=np.arange(12).reshape(2,2,3)
print(f'没有随机排列前的三维数组:\n{three_w}')
np.random.shuffle(three_w)
print(f'随机排列后的三维数组:\n{three_w}')