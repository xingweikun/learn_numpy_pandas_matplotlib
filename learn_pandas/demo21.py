import pandas as pd
path='./data_files/课件023-024/字符串.xlsx'
data=pd.read_excel(path)
print(data['姓名'].str.cat())#不指定参数，所有姓名拼接
print(data['姓名'].str.cat(sep='、'))
print(data['姓名'].str.cat(['变身']*len(data)))
print(data['姓名'].str.cat(['变身']*len(data),sep='^'))
print(data['姓名'].str.cat(['变身']*len(data),sep='^',na_rep='@'))

print(data['状态'].str.split()) # 不指定分隔符，就是一列表
print(data['状态'].str.split('血')) # 和python内置split一样
print(data['状态'].str.split('血',n=-1)) # 指定n，表示分隔次数，默认是-1，全部分隔
print(data['状态'].str.split('血',expand=True))
# 注意这个expand，默认是False，得到是一个列表
# 如果指定为True，会将列表打开，变成多列，变成DATAFrame
# 列名则是按照0 1 2 3····的顺序，并且默认Nan值分隔后还是为Nan
# 如果分隔符不存在，还是返回DATAFrame

print(data['状态'].str.partition('血'))# partition只会分隔一次
print('BbBbB'.partition('b'))
print(data['状态'].str.get(2))

print(data['状态'].str.slice(0)) # 指定一个值的话，相当于[m:]
print(data['状态'].str.slice(0,3)) # 相当于[m:n],从0开始不包括3
print(data['状态'].str.slice(0,3,2)) # 相当于[m: n: step]
print(data['状态'].str.slice(5,9,2)) # 索引越界，默认为空字符串，原来Nan还是Nan
print(data['状态'].str.slice_replace(1,3,"520"))
print(data['状态'].str.join('a'))
#contains 判断字符串是否含有指定子串，返回的是bool类型
print(data['状态'].str.contains('血')) # NaN还是返回Nan
print(data['状态'].str.contains('血',na=False))
print(data['状态'].str.contains('血',na=True))
print(data['状态'].str.contains('血',na="没有"))
print(data['状态'].str.startswith('满'))## NaN还是返回Nan，可按照 na= False 或 na = True 替
print(data['状态'].str.endswith('满'))
print(data['姓名'].str.repeat(3))
#pad 将每一个元素都用指定的字符填充，记住只能是一个字符
print(data['姓名'].str.pad(5,fillchar='&'))# 表示要占5个长度，用"&"填充,默认填在左边的
print(data['姓名'].str.pad(5,fillchar='<',side="right"))
print(data['姓名'].str.pad(5,fillchar='<',side="both"))#both两端
# 这三个是由pad变来的
"""
center(5, fillchar="<") <==> pad(5, size="both", fillchar="<")
ljust(5, fillchar="<") <==> pad(5, size="right", fillchar="<")
rjust(5, fillchar="<") <==> pad(5, size="left", fillchar="<")
"""
print(data['姓名'].str.zfill(10))#zfill 填充，只能是0，从左边填充
print(data['状态'].str.match(".{2}激"))
print(data["日期"].astype('str').str.extract("\d{4}-(\d{2})-(\d{2})"))#extract 分组捕获  加年(\d{4})
