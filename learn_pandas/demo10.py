import pandas as pd
url='./data_files/课件011/计算列.xlsx'
data=pd.read_excel(url,index_col='序号')
data['销售金额']=data['单价']*data['销售数量']
print(data)

url='./data_files/课件011/计算列.csv'
data=pd.read_csv(url,index_col='序号')
data['销售金额']=data['单价']*data['销售数量']
print(data)

url='./data_files/课件011/计算列.csv'
data=pd.read_csv(url,index_col='序号')
for i in range(1,3):
    data['销售金额'].at[i]=data['单价'].at[i]*data['销售数量'].at[i]
print(data)