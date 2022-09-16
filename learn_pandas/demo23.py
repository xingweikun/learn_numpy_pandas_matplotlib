import pandas as pd

path = './data_files/课件026/分组聚合.xlsx'
data = pd.read_excel(path)
for (i, j), group in data.groupby(['城市', '区']):
    print(i)  # 城市分组
    print(j)  # 区分组
    print(group)  # 城市和区的分组
path = './data_files/课件026/分组聚合2.xlsx'
data = pd.read_excel(path, index_col='店号')
dicts = {'1月': '一季度', '2月': '一季度', '3月': '一季度', '4月': '二季度'}
data2 = data.groupby(dicts, axis=1)
print(data2.sum())

path = './data_files/课件026/分组聚合3.xlsx'
data = pd.read_excel(path, index_col=[0, 1])
data3 = data.groupby(level='班级').mean()
print(data3)
