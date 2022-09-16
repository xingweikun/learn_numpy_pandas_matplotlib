import pandas as pd

path = './data_files/课件015-016/删除.xlsx'
data = pd.read_excel(path, index_col='序号')
# 删除行
print(data.drop(2))  # 删除单行，直接写行标签
print(data.drop(labels=[1, 3]))  # 删除多行，使用labels,标签写成列表
# 删除列
print(data.drop('语文', axis=1))  # 删除单列
print(data.drop(labels=['语文', '数学'], axis=1))  # 删除多列
# 凡是会对原数组作出修改并返回一个新数组的，往往都有一个 inplace可选参数。如果手动设定为True（默认为False），那么原数组直接就被替换。
# 而采用inplace=False之后，原数组名对应的内存值并不改变，需要将新的结果赋给一个新的数组或者覆盖原数组的内存位置。

print(data.isnull())  # 是缺失值就显示为T
print(data.notnull())  # 不是缺失值就显示为T

print(data.dropna())  # 删除有空值的行
print(data.dropna(axis=1))  # 删除有空值的列
print(data.dropna(how='all'))  # 删除所有值为Nan的行
print(data.dropna(thresh=2))  # 至少保留两个非缺失值
print(data.dropna(subset=['语文', '数学']))  # 在哪些列表中查看

print(data.fillna(0))  # 用常数填充
print(data.fillna({'语文': 0.1, '数学': 0.2, '英语': 0.3}))
'''
ffill 用前面的值填充
bfill 用后面的值填充
pad 向后填充
backfill 向前填充
'''
path = './data_files/课件015-016/填充.xlsx'
data = pd.read_excel(path)
print(data.fillna(method='ffill'))
print(data.fillna(method='ffill', limit=1))  # 只替换第1个值
