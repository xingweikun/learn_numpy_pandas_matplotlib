import pandas as pd

path = './data_files/课件017/数据统计.xlsx'
data = pd.read_excel(path, index_col='序号')
print(data.describe())
print(data['语文'].describe())
print(data['语文'].mean())
print(data['语文'].max())
print(data['语文'].min())
path = './data_files/课件018/去重.xlsx'
data = pd.read_excel(path, index_col='序号')
print(data['姓名'].unique())  # 唯一值
print(data['姓名'].value_counts())  # 姓名出现过几次
'''
keep：指定处理重复值的方法： 
first：保留第一次出现的值
last：保留最后一次出现的值
False：删除所有重复值，留下没有出现过重复的
'''
print(data.drop_duplicates(subset=['姓名'], keep='first'))  # 可以多列

print(data.duplicated())  # 判断重复行
print(data.duplicated(subset='姓名'))  # 判断某列重复数据
repeat_ = data.duplicated(subset='姓名')
print(data[repeat_])  # 提取重复
