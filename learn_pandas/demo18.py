import pandas as pd

path = './data_files/课件020/多层索引.xlsx'
data = pd.read_excel(path, index_col=[0, 1], sheet_name='有序')
print(data)
print(data.index)
print(data.index.levels[0])  # 对应外层索引
print(data.index.levels[1])  # 对应内层索引

# data = data.set_index('班级','序号') # 也可以这样设置分层索引
data2 = data.loc[('1班', slice(None)), :]  # 切片筛选index
print(data2)

data = pd.read_excel(path, index_col=[0, 1], sheet_name='无序')
print(data.index.is_lexsorted())  # 检查index是否有序
# 接下来，我们尝试对Index进行排序。（排序时要在level里指定index名）
data = data.sort_index(level='科目')
data2 = data.loc[('语文', slice(None)), :]
print(data2)
print('*' * 30)
多层索引 = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]], names=['x', 'y'])
print(多层索引)
多层索引 = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)], names=['x', 'y'])
print(多层索引)
多层索引 = pd.MultiIndex.from_product([['a', 'b'], [1, 2]], names=['x', 'y'])
print(多层索引)
# 未学完
