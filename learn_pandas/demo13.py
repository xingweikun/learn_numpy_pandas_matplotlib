import pandas as pd
path='./data_files/课件013-014/筛选.xlsx'
data=pd.read_excel(path,index_col='出生日期')
#语法：loc[行标签，列标签]
print(data.loc['1983-10-27','语文'])
print(data.loc['1983-10-27',['语文','数学','英语']])
print(data.loc['1983-10-27':'1990-12-31',['语文','数学','英语']])
print(data.loc[(data['语文']>60)&(data['英语']<60),:])#这里的 ,: 指的是列取全部

path='./data_files/课件013-014/条件判断.xlsx'
data=pd.read_excel(path,index_col='序号')
data.loc[data['性别']=="男","称呼"]="先生"
data.loc[data['性别']=="女","称呼"]="女士"
print(data)