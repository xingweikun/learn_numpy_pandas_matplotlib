import numpy as np
import pandas as pd
data1=pd.DataFrame({'姓名':['张三','李四','王五','李四','张三','张三'],'出手次数1':np.arange(6)})
data2=pd.DataFrame({'姓名':['赵六','王五','李四'],'出手次数2':[1,2,3]})
#内连接
data3=pd.merge(data1,data2)
print(f'data1:\n{data1}\ndata2:\n{data2}')
print(f'内连接:\n',data3)
# data4=pd.merge(data1,data2,on='姓名',how='inner')
# print(f'data4:\n',data4)
#左连接
data5=pd.merge(data1,data2,on='姓名',how='left')
print(f'左连接:\n',data5)
data6=pd.merge(data1,data2,on='姓名',how='right')
print(f'右连接:\n',data6)
data7=pd.merge(data1,data2,on='姓名',how='outer')
print(f'全连接:\n',data7)
data8=pd.DataFrame({'姓名':['张三','张三','王五'],'班级':['1班','2班','1班'],'分数':[10,20,30]})
data9=pd.DataFrame({'姓名':['张三','张三','王五','王五'],'班级':['1班','1班','1班','2班'],'分数':[40,50,60,70]})
data10=pd.merge(data8,data9,on=['姓名','班级'])#内连接
data11=pd.merge(data8,data9,on=['姓名','班级'],how='outer')#外连接
print(f'内连接:\n{data10}\n外连接:{data11}')
data12=pd.merge(data8,data9,on='姓名')#内连接
print(f'data12:\n',data12)
data13=pd.merge(data8,data9,on='姓名',suffixes=('_数据1','_数据2'))
print(f'data13:\n',data13)
data14 = pd.DataFrame({'姓名': ['张三','李四','王五','张三','李四'],'次数':range(5)})
data15 = pd.DataFrame({'数据': [10, 20]}, index=['张三','李四'])
data16=pd.merge(data14,data15,left_on='姓名',right_index=True)
print('data16\n',data16)
data17=pd.merge(data14,data15,left_on='姓名',right_index=True,how='outer')
print('data17\n',data17)