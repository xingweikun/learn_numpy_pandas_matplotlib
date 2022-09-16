# ## 参数
# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
# #### 参数说明
# axis：如果axis=0，那么by="列名"；如果axis=1，那么by="行号"；
# ascending:True则升序，可以是[True,False]，即第一字段升序，第二个降序
# inplace=True：不创建新的对象，直接对原始对象进行修改；
# inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。
# kind:排序方法，{‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’。似乎不用太关心
# na_position : {‘first’, ‘last’}, default ‘last’，默认缺失值排在最后面
import pandas as pd

path = './data_files/课件012/排序.xlsx'
data = pd.read_excel(path, index_col='序号')
# 按语文分数降序排列
data.sort_values(by='语文', inplace=True, ascending=False)
print(data)
# 按语文分数排序降序，数学升序，英语降序
data.sort_values(by=['语文', '数学', '英语'], inplace=True, ascending=[False, True, False])
print(data)
# 按索引进行排序
data.sort_index(inplace=True)
print(data)
print('*' * 30)
path = './data_files/课件012/排序进阶.xlsx'
data = pd.read_excel(path)
print(f'原表:\n{data}')
data.sort_values(by='a', inplace=True, ascending=False)
print(f'表1:\n{data}')
data = pd.read_excel(path)
data.sort_values(by=1, inplace=True, ascending=False, axis=1)
print(f'表2:\n{data}')
