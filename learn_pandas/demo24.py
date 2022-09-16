import pandas as pd

path = './data_files/课件027/分组.xlsx'
data = pd.read_excel(path)
# 按索引的奇偶行分组
data2 = data.groupby(data.index % 2 == 0)[['语文', '数学', '英语']].sum()
# 按前后5个分组
data3 = data.groupby(data.index >= 5)[['语文', '数学', '英语']].sum()
# 按姓氏或首字母分组
data4 = data.groupby(data.姓名.str[0])[['语文', '数学', '英语']].sum()
# 按姓名第1和第2个字或第1和第2个字母分组，注意两个str要写在列表中
data4_2 = data.groupby([data.姓名.str[0], data.姓名.str[1]])[['语文', '数学', '英语']].sum()
# 按指定班级分组（不需要全部班级时使用）
data5 = data.groupby(data.班级.isin(['1班', '2班']))[['语文', '数学', '英语']].sum()
# 按指定班级分组（不包括1班和2班的其它班级，记住~加的位置，没有isnotin函数）
data6 = data.groupby(~data.班级.isin(['1班', '2班']))[['语文', '数学', '英语']].sum()
# 按日期小时分组
data7 = data.groupby([data.时间.dt.date, data.时间.dt.hour])[['语文', '数学', '英语']].sum()
# 按日期中的年份分组
data8 = data.groupby([data.时间.dt.year])[['语文', '数学', '英语']].sum()
# 利用表格函数pipe直接使用分组方法
data9 = data.pipe(pd.DataFrame.groupby, '班级').sum()
print(data2)
