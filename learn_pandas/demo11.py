import pandas as pd

url = './data_files/课件011/apply函数.xlsx'
data = pd.read_excel(url, index_col='序号')
print(data)
data['加分'] = data['性别'].apply(lambda x: 5 if x != '男' else 0)
data['最终分数'] = data['总分'] + data['加分']
print(data)
url = './data_files/课件011/计算日期.xlsx'
data = pd.read_excel(url, index_col='序号')
data['间隔'] = data['结束日期'] - data['起始日期']
print(data)
