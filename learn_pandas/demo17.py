import pandas as pd

path = './data_files/课件019/计算.xlsx'
data = pd.read_excel(path)
result = data['1店'] + data['2店']
print(result)  # 无论加减乘除，结果都是 空值与数字计算 等于 空值
result = data['1店'].fillna(0) + data['2店'].fillna(0)
print(result)
result = data['1店'].add(data['2店'], fill_value=0)
print(result)

# 处理inf无穷大
result = data['1店'].div(data['2店'], fill_value=0)
print(result)

pd.options.mode.use_inf_as_na = True
path = './data_files/课件019/无穷大.xlsx'
data = pd.read_excel(path)
result = data['1店'].div(data['2店'], fill_value=0)
print(result)

path = './data_files/课件019/对齐.xlsx'
data1 = pd.read_excel(path, index_col='序号', sheet_name='Sheet1')
data2 = pd.read_excel(path, index_col='序号', sheet_name='Sheet2')
result = data1.add(data2, fill_value=0)
print(result.fillna(0))
