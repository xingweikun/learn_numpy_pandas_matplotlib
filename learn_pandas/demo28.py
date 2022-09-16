import pandas as pd

path = './data_files/课件030-031/数据2.xlsx'
data = pd.read_excel(path)
data2 = data.applymap(lambda x: "%.3f" % x)
print(data2)

# 行列转换
path = './data_files/课件030-031/转换.xlsx'
data = pd.read_excel(path)
data2 = pd.DataFrame(data.values.T, index=data.columns, columns=data.index)
print(data2)

path = './data_files/课件030-031/环比.xlsx'
data = pd.read_excel(path)
上月 = data.金额.shift()
同比 = 上月 - data.金额
data['同比'] = 同比
print(data)

数据 = pd.read_excel(path, 'Sheet2')


def 公式(新数据):
    新数据['环比'] = 新数据.金额.shift() - 新数据.金额
    return 新数据


数据2 = 数据.sort_values(['城市', '月份']).groupby('城市').apply(公式)
print(数据2)

path = './data_files/课件030-031/同比.xlsx'
data = pd.read_excel(path)
年 = data['日期'].dt.year
数据2 = pd.pivot_table(data, index='店号', values='金额', columns=年, aggfunc='sum')
同比 = (数据2[2019] - 数据2[2018]) / 数据2[2018]
数据2['同比'] = 同比
print(数据2)
