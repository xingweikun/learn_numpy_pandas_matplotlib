#填充常用类型数据
# 一、pd.read_excel参数：
# skiprows=行数 #跳过几行
# usecols="区域" # 和Excel中一样，就是一个列的区域
# index_col="字段名" # 将谁设置为索引
# dtype={'序号':str,'性别':str,'日期':str} # 防止出错，把类型全指定为字符型
# 二、数据.at的用法
# 作用：获取某个位置的值，例如，获取第0行，第a列的值，即：index=0，columns='a'
# 变量名 = 数据.at[0, 'a']
import pandas as pd
import datetime
url='./data_files/课件010/自动填充.xlsx'
begin_date=datetime.date(2020,1,1)#起始日期
data = pd.read_excel(url,skiprows=2,usecols="B:E",index_col=None,dtype={'序号':str,'性别':str,'日期':str})
def month_add(d,md):
    yd=md//12
    m=d.month+md%12
    if m !=12:
        yd+=m//12
        m=m%12
    return datetime.date(d.year+yd,m,d.day)
for i in data.index:
    data['序号'].at[i]=i+1
    data['性别'].at[i]='男' if i%2==0 else '女'
    # data['日期'].at[i]=begin_date+datetime.timedelta(days=i)#timedelta只能加天，小时，秒，毫秒
    # data['日期'].at[i]=datetime.date(begin_date.year+i,begin_date.month,begin_date.day)
    data['日期'].at[i]=month_add(begin_date,i)
data.set_index('序号',inplace=True)# 只在index上面改,不要生成新的
data.to_csv('./data_files/课件010/自动填充.csv',encoding='utf-8',index=False)
out_data=pd.read_csv('./data_files/课件010/自动填充.csv')
print(out_data)