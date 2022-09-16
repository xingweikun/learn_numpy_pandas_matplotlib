import pandas as pd

file01_url = './data_files/newfile01.xlsx'
data01 = pd.DataFrame()
data01.to_excel(file01_url, sheet_name='Sheet1', index=False)
print(f'{file01_url},创建成功')
file02_url = './data_files/newfile02.xlsx'
data02 = pd.DataFrame({'id': [1, 2, 3], '姓名': ['张三', '李四', '王五'], '年龄': [11, 12, 13]})
data02.to_excel(file02_url)
print(f'{file02_url},创建成功')
file03_url = './data_files/newfile03.xlsx'
data03 = pd.DataFrame({'id': [1, 2, 3], '姓名': ['张三', '李四', '王五'], '年龄': [11, 12, 13]})
data03 = data03.set_index('id')
data03.to_excel(file03_url)
print(f'{file03_url},创建成功')
