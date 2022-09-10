import pandas as pd
import os
#一个文件夹下多个工作簿的合并【单独Sheet】
path='./data_files/课件025/课件025/'
合并表=pd.DataFrame()
for file in os.listdir(path):
    table=pd.read_excel(path+file)
    合并表=pd.concat([合并表,table])
print(合并表)

path='./data_files/课件025/课件025-2/'
合并表=pd.DataFrame()
for file in os.listdir(path):
    table=pd.read_excel(path+file,header=1)
    合并表=pd.concat([合并表,table])
print(合并表)

#同一工作簿中多个Sheet合并
path='./data_files/课件025/课件025-3/合并2.xlsx'
数据 = pd.read_excel(path,None)
合并表 = pd.DataFrame()
字段名 = list(数据.keys()) # 返回['序号', '姓名', '电话']
for 列标签 in 字段名:
    新数据 = 数据[列标签]
    合并表 = pd.concat([合并表,新数据])
print(数据)
#将一个工作表拆分成多个工作表
路径 = './data_files/课件025/课件025-3/拆分.xlsx'
数据 = pd.read_excel(路径)
分割列 = list(数据['部门'].drop_duplicates()) # 返回：['办公室', '销售部', '保洁部']，笔记13.1
新数据 = pd.ExcelWriter('./data_files/课件025/课件025-3/多个Sheet.xlsx')
for i in 分割列:
    数据1 = 数据[数据['部门'] == i]
    数据1.to_excel(新数据,sheet_name=i)
新数据.save()
新数据.close()
#将一个工作表拆分成多个工作簿
路径 = './data_files/课件025/课件025-3/拆分.xlsx'
数据 = pd.read_excel(路径)
分割列 = list(数据['部门'].drop_duplicates()) # 返回：['办公室', '销售部', '保洁部']
for i in 分割列:
    数据1 = 数据[数据['部门'] == i]
    数据1.to_excel('./data_files/课件025/课件025-3/'+ i + '.xlsx')