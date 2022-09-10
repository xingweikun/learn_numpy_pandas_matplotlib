import pandas as pd
年份 = [1992, 1983, 1922, 1932, 1973] # 待分箱数据
箱子 = [1900, 1950, 2000] # 指定箱子的分界点
结果 = pd.cut(年份, 箱子)
print(结果)
print(pd.value_counts(结果)) # 对不同箱子中的数进行计数
# labels参数为False时，返回结果中用不同的整数作为箱子的指示符
结果2 = pd.cut(年份, 箱子,labels=False)
print(结果2)
print(pd.value_counts(结果2))

years=[1992,1983,1922,1932,1973]#待分箱数据
boxs=[1900,1950,2000]#指定箱子的分界点
# 可以将想要指定给不同箱子的标签传递给labels参数
box_names = ['50年代前','50年代后']
result3=pd.cut(years,boxs,labels=box_names)
print(result3)
print(pd.value_counts(result3))
#等频分箱
年份 = [1992, 1983, 1922, 1932, 1973, 1999, 1993, 1995] # 待分箱数据
结果 = pd.qcut(年份,q=4) # 参数q指定所分箱子的数量
# 从输出结果可以看到每个箱子中的数据量时相同的
print(结果)
print(pd.value_counts(结果)) # 从输出结果可以看到每个箱子中的数据量时相同的
