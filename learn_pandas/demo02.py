import pandas as pd

url = './data_files/课件001-005/读取文件.xlsx'
datas = pd.read_excel(url)
url = './data_files/课件001-005/读取文件.csv'
datas.to_csv(url, encoding='utf-8', index=False)
datas = pd.read_csv(url)
print(datas)
print(datas.head())  # 默认5行，指定行数写小括号里
print(datas.shape, '\n')  # 数据形状
print(datas.columns, '\n')  # 列名列表
print(datas.index, '\n')  # 索引列
print(datas.dtypes)  # 每一列数据类型
