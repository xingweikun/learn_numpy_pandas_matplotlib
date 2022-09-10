import pandas as pd
path='./data_files/课件028-029/Vlookup.xlsx'
data1=pd.read_excel(path,sheet_name='花名册')
data2=pd.read_excel(path,sheet_name='成绩单')
result=pd.merge(data1,data2.loc[:,['学号','总分']],how='left',on='学号')
print(result)
#如果要保存一个单独的表
path='./data_files/课件028-029/newfile.xlsx'
writer=pd.ExcelWriter(path)
result.to_excel(writer,index=False)
writer.save()
writer.close()

result_sum=result.总分
result=result.drop('总分',axis=1)
result.insert(0,'总分',result_sum)
print(result)