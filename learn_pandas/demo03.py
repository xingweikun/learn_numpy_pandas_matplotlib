import pandas as pd
path='./data_files/课件001-005/读取文件.csv'
datas=pd.read_csv(path,header=None,names=['序号','姓名','年龄','电话','地址','入职日期'],encoding='utf-8',index_col='序号')
print(datas)

import pymysql
conn_name=pymysql.connect(host='localhost',user='root',password='root',database='daxuepaiming',charset='utf8')
datas=pd.read_sql("select * from dxpm limit 5",con=conn_name)
print(datas)