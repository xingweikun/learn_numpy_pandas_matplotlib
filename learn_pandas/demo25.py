import numpy as np
import pandas as pd
path='./data_files/课件028-029/透视.xlsx'
data=pd.read_excel(path)
#index需要聚合的列名，默认情况下聚合所有数据值的列
data2=pd.pivot_table(data,index=['部门','销售人员'])
#values在结果透视的行上进行分组的列名或其它分组键【就是透视表里显示的列】
data3=pd.pivot_table(data,index=['部门','销售人员'],values=['数量','金额'])
#columns在结果透视表的列上进行分组的列名或其它分组键
data4=pd.pivot_table(data,index=['部门','销售人员'],values=['数量','金额'],columns='所属区域')
#Aggfunc聚合函数或函数列表（默认情况下是mean）可以是groupby里面的任意有效函数
data5=pd.pivot_table(data,index=['部门','销售人员'],values=['数量','金额'],columns='所属区域',aggfunc=[sum,np.mean])
'''
5、fill_value 在结果表中替换缺失值
例如：fill_value = 0
6、dropna 如果为True，将不含所有条目均为Na的列（默认为False）
dropna=True 
7、margins 添加行/列小计和总计 （默认为False）
margins =True
'''
# print(data5)

#交叉表 crosstab
data6=pd.crosstab([data.日期.dt.month,data.所属区域],data.部门,margins=True)
print(data6)