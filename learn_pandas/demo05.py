import pandas as pd
datas=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(datas)
print(datas['a'][0])
print(datas.iloc[0]['a'])
print(datas.iloc[0][0])
print(datas[['a', 'b']])
print('*'*30)
dicts={
    '姓名':['张三','李四','王五'],
    '年龄':[20,18,21],
    '爱好':['python','java','都不喜欢']
}
datas=pd.DataFrame(dicts)
print(datas)
print(datas.dtypes)
print(datas.columns)
print(datas.index)#起始，结束，步长
print('*'*30)
print(datas['姓名'])
print(type(datas['姓名']))
print(datas.loc[1])
print(type(datas.loc[1]))
print(datas[['姓名', '年龄']])
print(type(datas[['姓名', '年龄']]))
print(datas.loc[1:3])
print(type(datas.loc[1:3]))
print('*'*30)
data1=pd.Series(['张三','李四','王五'],index=[1,2,3],name='姓名')
data2=pd.Series(['男','男','男'],index=[1,2,3],name='性别')
data3=pd.Series([20,18,21],index=[1,2,3],name='年龄')
datas=pd.DataFrame({data1.name:data1,data2.name:data2,data3.name:data3})
print(datas)