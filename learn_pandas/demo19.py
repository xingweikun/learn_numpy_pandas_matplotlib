import pandas as pd

n="你好，Python!^你好，Pandas!你好，Python!^你好，Pandas!"
print(n.replace('Python','python'))
print(n.replace('Python','python',1))
print(n.replace('Python','python',10))
print(n)
path='./data_files/课件021/替换.xlsx'
data=pd.read_excel(path)
#整个表全部替换
data.replace('城八区','海淀区',inplace=True)
print(data)
#某一行替换
data=pd.read_excel(path)
data['城市2'].replace('城八区','海淀区',inplace=True)
print(data)
#替换指定的某个或多个数值（用字典的形式）

data=pd.read_excel(path)
dicts={'A':20,'B':30}
data.replace(dicts,inplace=True)
print(data)

data=pd.read_excel(path)
data.replace(['A','B'],[20,30],inplace=True)
print(data)

data=pd.read_excel(path)
data.replace(['A','B'],30,inplace=True)
print(data)

data=pd.read_excel(path)
data['城市']=data['城市'].str.replace('城八','市')
print(data)

data=pd.read_excel(path)
data.replace('[A-Z]',88,regex=True,inplace=True)
print(data)