import pandas as pd

path = './data_files/课件013-014/筛选.xlsx'
data = pd.read_excel(path, index_col='序号', sheet_name='Sheet1')
print(data)
print(data.loc[2:4])  # 2-4行数据
print(data[data['性别'] == '男'])
filter_conditions = "性别=='男' and 总分>=150"
print(data.query(filter_conditions))
filter_conditions = "姓名 in ['张伊','卢海军']"
print(data.query(filter_conditions))
# startswith( ) endwith( )
# startswith()函数
# 描述：判断字符串是否以指定字符或子字符串开头。
# 语法：str.endswith("suffix", start, end) 或 str[start,end].endswith("suffix") 用于判断字符串中某段字符串是否以指定字符或子字符串结尾。
# —> bool 返回值为布尔类型（True,False）
# start —索引字符串的起始位置。
# end — 索引字符串的结束位置。
# str.endswith(suffix) star默认为0，end默认为字符串的长度减一（len(str)-1）
# suffix — 后缀，可以是单个字符，也可以是字符串，还可以是元组（"suffix"中的引号要省略）。
# 注意：空字符的情况。返回值通常也为True
filter_conditions = data['姓名'].str.startswith('王')
print(data[filter_conditions])

# str.contains(pat, case=True, flags=0, na=nan, regex=True)是否包含查找的字符串
# 参数:
# pat : 字符串/正则表达式
# case : 布尔值, 默认为True.如果为True则匹配敏感
# flags : 整型,默认为0(没有flags)
# na : 默认为NaN,替换缺失值.
# regex : 布尔值, 默认为True.如果为真则使用re.research,否则使用Python
# 返回值:
# 布尔值的序列(series)或数组(array)
filter_conditions = data['地址'].str.contains('信阳市')
print(data[filter_conditions])
filter_conditions = data['地址'].str.contains('[a-cA-C]座')
print(data[filter_conditions])
filter_conditions = "60 <= 语文 <= 100 and 性别=='女'"
print(data.query(filter_conditions))
data = pd.read_excel(path, index_col='出生日期', parse_dates=['出生日期'])  # 将出生日期列转成日期格式
print(data['1989'].head())
print(data['1983-10'].head())
data2 = data.sort_values('出生日期')
print('*' * 30)
# 获取某个时期之前或之后的数据
# 获取1980年以后的数据
print(data2.truncate(before='1980').head())
# 获取1990-12之前的数据
print(data2.truncate(after='1990-12').head())
# 获取1990-02年以后的数据
print(data2.truncate(before='1990-02').head())
# 获取1984-01-01年以后的数据
print(data2.truncate(before='1984-01-1').head())
# 获取指定时间区间
print(data2['1983':'1990'])
print(data2['1983-01-1':'1990-12-31'])
# 获取指定年月日和时间
print(data2.truncate(after='1984-01-1 16:00:00').head())
data = pd.read_excel(path, index_col='序号', parse_dates=['出生日期'])
filter_conditions = (
    '@data.出生日期.dt.year>1980 and'
    '@data.出生日期.dt.year<1990'
    'and 性别=="男"'
)
print(data.query(filter_conditions))
