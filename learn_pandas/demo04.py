import pandas as pd

datas = pd.Series(['张三', 19, '2001-10'])
print(datas)
print(datas.index)
print(datas.values)
print('*' * 30)
datas = pd.Series(['张三', 19, '2001-10'], index=['a', 'b', 'c'])
print(datas)
print(datas.index)
print('*' * 30)
dicts = {'姓名': '张三', '年龄': 19, '出生日期': '2001-10'}
datas = pd.Series(dicts)
print(datas)
print(datas.index)
print('*' * 30)
print(datas['姓名'])
print(datas[['姓名', '年龄']])
print(type(datas[['姓名', '年龄']]))
print('*' * 30)
data1 = ['姓名', '年龄', '出生日期']
data2 = ['张三', '19', '2001-10']
datas = pd.Series(data2, index=data1)
print(datas)
print(datas.sort_index)
print(datas.sort_values)
